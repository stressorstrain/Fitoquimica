# Generated by Django 2.1.3 on 2018-12-13 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectdocs',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectdocs',
            name='user',
        ),
        migrations.DeleteModel(
            name='ProjectDocs',
        ),
    ]
