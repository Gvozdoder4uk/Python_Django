from django.db import models


# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    post = models.TextField(verbose_name='Тело статьи')
    date = models.DateTimeField(verbose_name='Время')
    image = models.FileField(verbose_name='Картинка')

    def __str__(self):
        return self.title


class EP_Keys(models.Model):
    id_key = models.BigIntegerField(verbose_name="Номер ключа")
    owner = models.TextField(verbose_name="Владелец ключа")
    date_create = models.DateTimeField(verbose_name="Дата выпуска ЭП")
    date_expired = models.DateTimeField(verbose_name="Дата окончания ЭП")
    for_services = models.TextField(verbose_name="Принадлежность к сервису")
    comment = models.TextField(verbose_name="Комментарий", blank=True)
    user_photo = models.FileField(verbose_name="Фото пользователя", blank=True)
    license_csp = models.CharField(max_length=120, verbose_name="Лицензия CSP")
    license_tsp = models.CharField(max_length=120, verbose_name="Лицензия TSP")
    license_ocsp = models.CharField(max_length=120, verbose_name="Лицензия OCSP")

    def __str__(self):
        return self.owner
