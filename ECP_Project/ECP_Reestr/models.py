from django.db import models


# Create your models here.
class Visual(models.Model):
    class Meta:
        db_table = 'wallapers'

    img = models.CharField(max_length=120, verbose_name='Файл картинки')
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Описание')
    alt = models.TextField(verbose_name='Подсказка')
    index = models.IntegerField(verbose_name='Индекс')

    def __unicode__(self):
        return self.title
