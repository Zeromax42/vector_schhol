# Generated by Django 3.2.3 on 2021-05-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vectorapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(max_length=3, verbose_name='Класс'),
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]
