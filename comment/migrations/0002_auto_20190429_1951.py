# Generated by Django 2.1.7 on 2019-04-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='url',
        ),
        migrations.AlterField(
            model_name='comment',
            name='Email',
            field=models.EmailField(help_text='请填入你的邮箱', max_length=255),
        ),
    ]
