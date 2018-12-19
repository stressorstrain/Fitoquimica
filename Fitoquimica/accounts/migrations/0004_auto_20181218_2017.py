# Generated by Django 2.1.2 on 2018-12-18 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_projectdocs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expequip',
            name='exp',
        ),
        migrations.RemoveField(
            model_name='expsupplies',
            name='exp',
        ),
        migrations.RemoveField(
            model_name='exptodo',
            name='exp',
        ),
        migrations.RemoveField(
            model_name='userexperiments',
            name='user',
        ),
        migrations.DeleteModel(
            name='ExpEquip',
        ),
        migrations.DeleteModel(
            name='ExpSupplies',
        ),
        migrations.DeleteModel(
            name='ExpToDo',
        ),
        migrations.DeleteModel(
            name='UserExperiments',
        ),
    ]