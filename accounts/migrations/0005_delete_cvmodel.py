# Generated by Django 3.1.1 on 2020-09-06 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_cvmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CvModel',
        ),
    ]