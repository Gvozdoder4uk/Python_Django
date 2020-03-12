from django.db import models
import openpyxl
from django.contrib import admin
from django.shortcuts import render

class Services(models.Model):
    service_name = models.CharField(max_length=200, help_text="Введите название сервиса",
                                    verbose_name="Наименование сервиса")

    def __str__(self):
        return self.service_name


class EP_Keys(models.Model):
    class Meta:
        ordering = ['-date_create']

    id_key = models.BigIntegerField(verbose_name="Номер ключа")
    owner = models.TextField(verbose_name="Владелец ключа")
    date_create = models.DateTimeField(verbose_name="Дата выпуска ЭП")
    date_expired = models.DateTimeField(verbose_name="Дата окончания ЭП")
    comment = models.TextField(verbose_name="Комментарий", blank=True)
    user_photo = models.FileField(verbose_name="Фото пользователя", blank=True)
    license_csp = models.CharField(max_length=120, verbose_name="Лицензия CSP", blank=True, default="Не выделена")
    license_tsp = models.CharField(max_length=120, verbose_name="Лицензия TSP", blank=True, default="Не выделена")
    license_ocsp = models.CharField(max_length=120, verbose_name="Лицензия OCSP", blank=True, default="Не выделена")
    for_services = models.ManyToManyField(Services, help_text='Select a genre for this book',
                                          verbose_name="Принадлежность к сервису")

    def __str__(self):
        return self.owner

class Service_Catalog(models.Model):
    service_name = models.CharField(max_length=200, help_text="Введите название сервиса",
                                    verbose_name="Наименование сервиса")

    def __str__(self):
        return self.service_name

