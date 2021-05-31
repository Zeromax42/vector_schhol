from django.db import models
from django.conf import settings
from django.utils import timezone
import django_filters

class Student (models.Model):
    first_name = models.CharField(max_length=40, verbose_name='Имя')
    last_name = models.CharField(max_length=40, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=40, verbose_name='Отчество')
    age = models.IntegerField(verbose_name='Возраст')
    grade = models.CharField(max_length=3, verbose_name='Класс')
    school_name = models.CharField(max_length=150, verbose_name='Школа')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
                'last_name': ['icontains'],
                'first_name': ['icontains'],
                'age': ['icontains'],
             }
        order_by = ['last_name']


class Teacher (models.Model):
    first_name = models.CharField(max_length=40, verbose_name='Имя')
    last_name = models.CharField(max_length=40, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=40, verbose_name='Отчество')
    school_name = models.CharField(max_length=150, verbose_name='Школа')
    disc = models.ManyToManyField('Disciplines')

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

class Disciplines (models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    student = models.ManyToManyField('Student')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

class Articles (models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=150, verbose_name='Название новости')
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField(verbose_name='Текст новости')
    published_date = models.DateTimeField(blank=True, null=True)
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
