# Generated by Django 3.1.4 on 2020-12-28 09:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0002_auto_20201228_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileall',
            name='file',
            field=models.FileField(upload_to='files/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'pptx'])]),
        ),
    ]
