# Generated by Django 2.1.2 on 2018-11-29 12:10

import commom.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commom', '0002_auto_20181125_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriasProtocolos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(default='Extração', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Protocolos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_name', models.CharField(default='Método', max_length=20)),
                ('file', models.FileField(upload_to=commom.models.protocol_directory_path)),
                ('method_class', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='commom.CategoriasProtocolos')),
            ],
        ),
    ]
