import datetime
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from rangefilter.filters import DateRangeFilter
from .resources import GVSResource
from django.http import HttpResponse
from django.http import HttpResponse
from datetime import date
from django.contrib import messages
from django.utils.translation import ngettext


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    @admin.action(description='Отметить выбранные сообщения как прочитанные')
    def make_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, ngettext(
            '%d сообщения успешно отмечены на прочитанные.',
            '%d сообщений успешно отмечены на прочитанные.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Отметить выбранные сообщения как непрочитанные')
    def make_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, ngettext(
            '%d сообщения успешно отмечены на непрочитанные.',
            '%d сообщений успешно отмечены на непрочитанные.',
            updated,
        ) % updated, messages.SUCCESS)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    list_display = ('id', 'name', 'message_type',
                    'email', 'income_date', 'is_read')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email', 'message_type', 'message')
    fields = ('name', 'email', 'message_type', 'message')
    readonly_fields = ('name', 'message_type', 'email', 'message')
    list_filter = ('is_read', 'message_type', ('income_date', DateRangeFilter)
                   )
    date_hierarchy = 'income_date'
    list_editable = ['is_read']
    actions = [make_unread, make_read]

    def get_rangefilter_income_date_default(self, request):
        return (datetime.date.today, datetime.date.today)


class NewsAdmin(admin.ModelAdmin):

    @admin.action(description='Отметить выбранные новости как опубликованные')
    def make_published(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, ngettext(
            '%d новости успешно отмечены как опубликованные.',
            '%d новостей успешно отмечены как опубликованные.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Отметить выбранные новости как неопубликованные')
    def make_unpublished(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, ngettext(
            '%d новости успешно отмечены как неопубликованные.',
            '%d новостей успешно отмечены как неопубликованные.',
            updated,
        ) % updated, messages.SUCCESS)

    list_display = ('id', 'title', 'time_create',
                    'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'brief', 'content')
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'brief', 'content', 'photo', 'get_html_photo',
              'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    list_filter = ('is_published', ('time_create', DateRangeFilter), ('time_update', DateRangeFilter),
                   )
    date_hierarchy = 'time_create'
    actions = [make_unpublished, make_published]

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=100")

    get_html_photo.short_description = "Миниатюра"

    def get_rangefilter_time_create_default(self, request):
        return (datetime.date.today, datetime.date.today)

    def get_rangefilter_time_update_default(self, request):
        return (datetime.date.today, datetime.date.today)


def export_xls(modeladmin, request, queryset):

    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=GVSFullList_' + \
        str(date.today())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(
        'Информация по ГВС ' + str(date.today()))

    font_style = xlwt.XFStyle()
    font_style.font.height = 225
    font_style.alignment.wrap = 1
    font_style.alignment.horz = xlwt.Alignment.HORZ_RIGHT
    font_style.alignment.vert = xlwt.Alignment.VERT_BOTTOM
    font_style.font.name = 'Times New Roman'
    alignment = xlwt.Alignment()
    alignment.vert = 0x01
    alignment.horz = 0x00

    ws.write_merge(
        2, 2, 9, 11, "«УТВЕРЖДАЮ»", font_style)

    font_style = xlwt.XFStyle()
    font_style.font.height = 225
    font_style.alignment.wrap = 1
    font_style.alignment.horz = xlwt.Alignment.HORZ_RIGHT
    font_style.alignment.vert = xlwt.Alignment.VERT_BOTTOM
    font_style.font.name = 'Times New Roman'
    alignment = xlwt.Alignment()
    alignment.vert = 0x01
    alignment.horz = 0x00

    ws.write_merge(
        3, 3, 9, 11, "Зам. генерального директора", font_style)

    font_style = xlwt.XFStyle()
    font_style.font.height = 225
    font_style.alignment.wrap = 1
    font_style.alignment.horz = xlwt.Alignment.HORZ_RIGHT
    font_style.alignment.vert = xlwt.Alignment.VERT_BOTTOM
    font_style.font.name = 'Times New Roman'
    alignment = xlwt.Alignment()
    alignment.vert = 0x01
    alignment.horz = 0x00

    ws.write_merge(
        4, 4, 9, 11, "по производству – главный инженер", font_style)

    font_style = xlwt.XFStyle()
    font_style.font.height = 225
    font_style.alignment.wrap = 1
    font_style.alignment.horz = xlwt.Alignment.HORZ_RIGHT
    font_style.alignment.vert = xlwt.Alignment.VERT_BOTTOM
    font_style.font.name = 'Times New Roman'
    alignment = xlwt.Alignment()
    alignment.vert = 0x01
    alignment.horz = 0x00

    ws.write_merge(
        5, 5, 9, 11, "___________________С.А. Панихин", font_style)

    font_style = xlwt.XFStyle()
    font_style.font.height = 225
    font_style.alignment.wrap = 1
    font_style.alignment.horz = xlwt.Alignment.HORZ_RIGHT
    font_style.alignment.vert = xlwt.Alignment.VERT_BOTTOM
    font_style.font.name = 'Times New Roman'
    alignment = xlwt.Alignment()
    alignment.vert = 0x01
    alignment.horz = 0x00

    ws.write_merge(
        6, 6, 9, 11, "«_______»___________________2022г.", font_style)

    font_style = xlwt.XFStyle()
    font_style.font.height = 225
    font_style.alignment.wrap = 1
    font_style.font.bold = True
    font_style.alignment.horz = xlwt.Alignment.HORZ_CENTER
    font_style.alignment.vert = xlwt.Alignment.VERT_CENTER
    font_style.font.name = 'Times New Roman'
    alignment = xlwt.Alignment()
    alignment.vert = 0x01
    alignment.horz = 0x01
    ws.write_merge(
        12, 13, 2, 9, "Перечень многоэтажных жилых домов, где отсутствует горячее водоснабжение по состоянию на " + str(date.today()), font_style)

    row_num = 15

    font_style = xlwt.XFStyle()
    font_style.font.height = 225
    font_style.alignment.wrap = 1
    font_style.font.bold = True
    font_style.alignment.horz = xlwt.Alignment.HORZ_CENTER
    font_style.alignment.vert = xlwt.Alignment.VERT_CENTER
    font_style.font.name = 'Times New Roman'
    font_style.borders.top = 1
    font_style.borders.right = 1
    font_style.borders.left = 1
    font_style.borders.bottom = 1
    alignment = xlwt.Alignment()
    alignment.vert = 0x01
    alignment.horz = 0x01

    columns = ['№ п/п', "ТК,НО, ЦТП", 'Сетевой район', 'Улица', 'Дом', 'Дата отключения',
               'Ориентир. дата устранения', 'Причина']

    ws.col(2).width = 2200  # №
    ws.col(3).width = 3000  # ТК,НО, ЦТП
    ws.col(4).width = 6000  # Сетевой район
    ws.col(5).width = 6000  # Улица
    ws.col(6).width = 2000  # Дом
    ws.col(7).width = 4200  # Дата отключения
    ws.col(8).width = 4200  # Ориентир. дата подключения
    ws.col(9).width = 8000  # Причина

    for col_num in range(len(columns)):
        ws.write(row_num, col_num + 2, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    font_style.font.height = 225
    font_style.alignment.wrap = 1
    font_style.alignment.horz = xlwt.Alignment.HORZ_CENTER
    font_style.alignment.vert = xlwt.Alignment.VERT_CENTER
    font_style.font.name = 'Times New Roman'
    font_style.borders.top = 1
    font_style.borders.right = 1
    font_style.borders.left = 1
    font_style.borders.bottom = 1
    alignment = xlwt.Alignment()
    alignment.vert = 0x01
    alignment.horz = 0x01

    count = 0
    for obj in queryset:
        row_num += 1
        count += 1
        row = [
            obj.pk,
            obj.rem_obj,
            obj.region,
            obj.street,
            obj.build,
            obj.date_disconnect,
            obj.date_connect,
            obj.reason,
        ]

        for col_num in range(len(row)):
            ws.write(row_num, col_num + 2, str(row[col_num]), font_style)

    font_style = xlwt.XFStyle()
    font_style.font.height = 225
    font_style.alignment.wrap = 1
    font_style.font.bold = True
    font_style.alignment.horz = xlwt.Alignment.HORZ_CENTER
    font_style.alignment.vert = xlwt.Alignment.VERT_CENTER
    font_style.font.name = 'Times New Roman'
    font_style.borders.top = 1
    font_style.borders.right = 1
    font_style.borders.left = 1
    font_style.borders.bottom = 1
    alignment = xlwt.Alignment()
    alignment.vert = 0x01
    alignment.horz = 0x01

    ws.write_merge(row_num + 1, row_num + 1, 2, 2, "", font_style)
    ws.write_merge(row_num + 1, row_num + 1, 3, 3, "Итого:", font_style)
    ws.write_merge(row_num + 1, row_num + 1, 4, 4, count, font_style)
    ws.write_merge(row_num + 1, row_num + 1, 5, 5, "", font_style)
    ws.write_merge(row_num + 1, row_num + 1, 6, 6, "", font_style)
    ws.write_merge(row_num + 1, row_num + 1, 7, 7, "", font_style)
    ws.write_merge(row_num + 1, row_num + 1, 8, 8, "", font_style)
    ws.write_merge(row_num + 1, row_num + 1, 9, 9, "", font_style)

    wb.save(response)
    return response


export_xls.short_description = u"Экспортировать в Excel (.xls)"


class GVSAdmin(admin.ModelAdmin):

    @admin.action(description='Отметить выбранные элементы как опубликованные')
    def make_published(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, ngettext(
            '%d элементы успешно отмечены как опубликованные.',
            '%d элементов успешно отмечены как опубликованные.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Отметить выбранные элементы как неопубликованные')
    def make_unpublished(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, ngettext(
            '%d элементы успешно отмечены как неопубликованные.',
            '%d элементов успешно отмечены как неопубликованные.',
            updated,
        ) % updated, messages.SUCCESS)

    list_display = ('id', 'rem_obj', 'region', 'street', 'build',
                    'date_disconnect', 'date_connect', 'reason', 'is_published')
    search_fields = ('region', 'rem_obj', '^street', '^build',
                     'date_disconnect', 'date_connect')
    list_editable = ('date_connect', 'reason', 'is_published')
    list_filter = ('region', 'reason', ('date_disconnect', DateRangeFilter),
                   ('date_connect', DateRangeFilter),)
    date_hierarchy = 'date_disconnect'
    actions = [make_unpublished, make_published, export_xls]

    # resource_class = GVSResource

    def get_rangefilter_date_disconnect_default(self, request):
        return (datetime.date.today, datetime.date.today)

    def get_rangefilter_date_connect_default(self, request):
        return (datetime.date.today, datetime.date.today)


admin.site.empty_value_display = 'Пусто'

admin.site.register(News, NewsAdmin)
admin.site.register(GVS, GVSAdmin)

admin.site.site_title = 'Админ-панель ТОО "ПТС"'
admin.site.site_header = 'Админ-панель ТОО "ПТС"'
