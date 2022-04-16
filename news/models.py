
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL(slug)")
    brief = models.TextField(blank=False, verbose_name="Краткое описание")
    content = RichTextField(blank=False, verbose_name="Контент")
    photo = models.ImageField(
        upload_to='photos/%Y-%m-%d', verbose_name="Фото", blank=True)
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(
        auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('new', kwargs={'new_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['time_create', 'title']


class GVS(models.Model):
    street = models.CharField(verbose_name='Улица', max_length=50)
    build = models.CharField(verbose_name='Дом', max_length=50)
    REGIONS = (
        ('Северный сетевой район', 'Северный сетевой район'),
        ('Южный сетевой район', 'Южный сетевой район'),
    )
    rem_obj = models.CharField(
        verbose_name='ТК,НО, ЦТП', max_length=50, default='')
    region = models.CharField(
        verbose_name='Сетевой район', max_length=50, choices=REGIONS)
    date_disconnect = models.DateField(verbose_name="Дата отключения")
    date_connect = models.DateField(
        verbose_name="Ориентировочная дата устранения")
    reason = models.CharField(
        verbose_name='Причина отсутствия ГВС', max_length=250)
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return f'{self.region} {self.street} {self.build}'

    class Meta:
        verbose_name = 'Элемент списка'
        verbose_name_plural = 'Список домов Северного и Южного сетевых районов, в которых отсутствует ГВС'
        ordering = ['id', 'region', 'street', 'build']


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    email = models.EmailField(max_length=200, verbose_name="E-mail")
    MT = (
        ('Общие вопросы', 'Общие вопросы'),
        ('Претензии|Жалобы|Замечания к работе',
         'Претензии|Жалобы|Замечания к работе'),
        ('Диспетчерская служба', 'Диспетчерская служба'),
        ('Тепловая инспекция', 'Тепловая инспекция'),
    )
    message_type = models.CharField(
        max_length=50, choices=MT, default="Выберите тип сообщения", verbose_name="Тип сообщения")
    message = models.TextField(max_length=1000, verbose_name="Текст сообщения")
    income_date = models.DateField(auto_now=True, verbose_name="Дата")
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Элемент обратной связи'
        verbose_name_plural = 'Обратная связь'
        ordering = ['id', 'name', 'email']
