# Generated by Django 3.0 on 2021-08-03 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_document_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='materia',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='documents/%materia/%Y/%m/%d'),
        ),
    ]
