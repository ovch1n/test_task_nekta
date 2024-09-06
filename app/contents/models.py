from django.db import models
from django.contrib.auth.models import User

class Request(models.Model):
    title = models.CharField(
                             verbose_name = ('Заголовок'),
                             max_length=255
                            )
    content = models.TextField(
                               verbose_name = ('Текст'),
                               max_length=2555,
                               blank=True,
                               null=True,
                              )
    user = models.ForeignKey(
                             User,
                             verbose_name = ('Пользователь'),
                             on_delete=models.CASCADE
                            )
    created_at = models.DateTimeField(
                                      verbose_name = ('Дата и время создания'),
                                      auto_now_add=True
                                     )
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']

class RequestMessage(models.Model):
    request = models.ForeignKey(
                                Request,
                                verbose_name = ('Заявка'),
                                related_name='messages',
                                on_delete=models.CASCADE,
                               )
    content = models.TextField(
                               verbose_name = ('Текст')
                              )
    user = models.ForeignKey(
                             User,
                             verbose_name = ('Пользователь'),
                             on_delete=models.CASCADE
                            )
    created_at = models.DateTimeField(
                                      verbose_name = ('Дата и время создания'),
                                      auto_now_add=True
                                     )
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']
