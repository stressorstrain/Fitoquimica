# Generated by Django 2.1.3 on 2018-11-23 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cromatografia', '0003_auto_20181123_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gas',
            options={'verbose_name_plural': 'Gases'},
        ),
        migrations.RemoveField(
            model_name='gas',
            name='created_at',
        ),
    ]
