from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField('Заголовок', max_length=50, null=False)
    image = models.ImageField('Картинка', upload_to='about_us')
    text1 = models.TextField('Текст 1')
    title2 = models.CharField('Почему мы?', max_length=50, null=False)
    text2 = models.TextField('Мы текст')
    title3 = models.CharField('Наши приемущества', max_length=50, null=False)
    text3 = models.TextField('Приемущества текст')
    title4 = models.CharField('Наши услуги', max_length=50, null=False)
    text4 = models.TextField('Услуги текс')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class ContactUs(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Email', max_length=50)
    phone = models.CharField('Телефон', max_length=50)
    message = models.TextField('Сообщение')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Contacts(models.Model):
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email', max_length=50)
    address = models.CharField('Адресс', max_length=200)

    class Meta:
        verbose_name = 'Контактс'
        verbose_name_plural = 'Контактсы'
