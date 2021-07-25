# Generated by Django 2.2.2 on 2021-07-25 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ManyToManyField(to='news.Comment', verbose_name='Тэг'),
        ),
    ]