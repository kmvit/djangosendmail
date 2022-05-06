import pytz
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
import datetime


class Mailing(models.Model):
    date_start = models.DateTimeField(verbose_name='Дата начала рассылки')
    date_end = models.DateTimeField(verbose_name='Дата окончание рассылки')
    content = models.TextField(max_length=255, verbose_name='Сообщение')
    tag = models.CharField(max_length=100, blank=True, verbose_name='Тэги')
    operator_code = models.CharField(max_length=3, blank=True, verbose_name='Кода оператора')

    @property
    def get_send(self):
        now = timezone.now()
        if self.date_start <= now <= self.date_end:
            return True
        else:
            return False

    def __str__(self):
        return f'Рассылка {self.id} - начало {self.date_start} / конец {self.date_end} - {timezone.now()} '

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Client(models.Model):
    regex = RegexValidator(regex=r'^7\d{10}$',
                                 message="Номер клиента в формате 7XXXXXXXXXX (X - номер от 0 до 9)")
    phone_number = models.CharField(verbose_name='Номер телефона', validators=[regex], unique=True, max_length=11)
    operator_code = models.CharField(verbose_name='Код оператора', max_length=3)
    tag = models.CharField(verbose_name='Тэги', max_length=100, blank=True)
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    timezone = models.CharField(verbose_name='Временная зона', max_length=32, choices=TIMEZONES, default='UTC')

    def save(self, *args, **kwargs):
        self.operator_code = str(self.phone_number)[1:4]
        return super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return f'Телефон-{self.phone_number}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    STATUS_CHOICES = [
        ('SEND', "Send"),
        ('NO_SEND', "No send"),
    ]

    time_create = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    status = models.CharField(verbose_name='Статус', max_length=15, choices=STATUS_CHOICES)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='сообщение')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='клиент')

    def __str__(self):
        return f'Сообщение {self.id}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'