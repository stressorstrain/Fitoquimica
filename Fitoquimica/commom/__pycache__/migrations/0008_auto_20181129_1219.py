# Generated by Django 2.1.2 on 2018-11-29 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commom', '0007_protocolos_method_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocolos',
            name='method_class',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='commom.CategoriasProtocolos'),
        ),
    ]
