# Generated by Django 5.0.2 on 2024-02-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок записи')),
                ('description', models.TextField(verbose_name='Текст записи')),
                ('author', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('date', models.DateField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
