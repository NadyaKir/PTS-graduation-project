from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .forms import ContactForm
from .models import *
from django.core.paginator import Paginator
from .filters import FindGVSItem
import xlwt
from datetime import date
from django.template.loader import get_template


def index(request):
    last_news = News.objects.filter(
        is_published=True).order_by("-time_create")[0:3]

    result = GVS.objects.filter(
        is_published=True).order_by('region', 'street').distinct()

    myFilter = FindGVSItem(request.GET, queryset=result)
    result = myFilter.qs

    context = {
        'last_news': last_news,

        'title': 'ТОО "Павлодарские тепловые сети"',
        'results_list': result,
        'myFilter': myFilter
    }

    return render(request, 'news/index.html', context)


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=GVSFullList_' + \
        str(date.today())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Информация на ' + str(date.today()))

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.font.height = 280
    font_style.alignment.wrap = 1
    font_style.alignment.horz = xlwt.Alignment.HORZ_CENTER
    font_style.font.name = 'Times New Roman'

    ws.write_merge(
        1, 1, 2, 8, "Перечень многоэтажных жилых домов, где отсутствует горячее водоснабжение по состоянию на " + str(date.today()), font_style)

    row_num = 5
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.alignment.wrap = 1
    font_style.font.height = 240
    font_style.borders.top = 1
    font_style.borders.right = 1
    font_style.borders.left = 1
    font_style.borders.bottom = 1
    font_style.alignment.horz = xlwt.Alignment.HORZ_CENTER

    columns = ['№ п/п', 'Сетевой район', 'Улица', 'Дом', 'Дата отключения',
               'Ориентир. дата устранения', 'Причина']

    ws.col(2).width = 1200  # №
    ws.col(3).width = 8000  # Сетевой район
    ws.col(4).width = 6000  # Улица
    ws.col(5).width = 2000  # Дом
    ws.col(6).width = 4000  # Дата отключения
    ws.col(7).width = 4000  # Ориентир. дата подключения
    ws.col(8).width = 15000  # Причина

    for col_num in range(len(columns)):
        ws.write(row_num, col_num + 2, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    font_style.font.height = 240
    font_style.alignment.wrap = 1
    font_style.borders.top = 1
    font_style.borders.right = 1
    font_style.borders.left = 1
    font_style.borders.bottom = 1
    font_style.font.name = 'Times New Roman'
    font_style.alignment.horz = xlwt.Alignment.HORZ_CENTER

    rows = GVS.objects.all().values_list('id', 'region', 'street', 'build',
                                         'date_disconnect', 'date_connect', 'reason')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num + 2, str(row[col_num]), font_style)
    wb.save(response)

    return response


def news(request):
    news_items = News.objects.filter(
        is_published=True).order_by("-time_create")

    paginator = Paginator(news_items, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Новости',
        'page_obj': page_obj,
    }

    return render(request, 'news/news.html', context)


def show_new(request, new_slug):
    new = get_object_or_404(News, slug=new_slug)

    context = {
        'new': new,
        'title': new.title,
    }

    return render(request, 'news/new.html', context=context)


def tariffs(request):

    context = {
        'title': 'Тарифы',
    }
    return render(request, 'news/tariff.html', context)


def contacts(request):
    context = {
        'title': 'Контакты',
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_message(
                form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'success': 1}

    else:
        form = ContactForm()

    context['form'] = form

    return render(request, 'news/contacts.html', context=context)


def send_message(name, email, message):
    text = get_template('news/message.html')
    html = get_template('news/message.html')
    context = {'name': name, 'email': email, 'message': message}
    subject = 'Сообщение от пользователя'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [
                                 'admin@example.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def success(request):
    return HttpResponse('Письмо отправлено!')


def about(request):

    context = {
        'title': 'Общая информация',
    }

    return render(request, 'news/about.html', context)


def director(request):

    context = {
        'title': 'Руководитель',
    }

    return render(request, 'news/director.html', context)


def requisites(request):

    context = {
        'title': 'Реквизиты',
    }

    return render(request, 'news/requisites.html', context)


def consumerinfo(request):
    context = {
        'title': 'Потребителям',
    }

    return render(request, 'news/consumerinfo.html', context)


def sitemap(request):
    context = {
        'title': 'Карта сайта',
    }

    return render(request, 'news/sitemap.html', context)


def pageNotFound(request, exception):
    return render(request, 'news/404.html', status=404)


def userguide(request):
    context = {}
    return(request, 'news/404.html', context)


def search(request):

    if request.method == "POST":
        searched = request.POST['q']
        news_list = News.objects.raw('SELECT * FROM news_news WHERE title iLIKE %s OR brief iLIKE %s OR content iLIKE %s', [
            '%'+searched+'%', '%'+searched+'%', '%'+searched+'%'])

    paginator = Paginator(news_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news/search.html',  {'searched':  searched, 'title': 'Результаты поиска',  'page_obj': page_obj, })
