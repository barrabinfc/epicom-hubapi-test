# Generated by Django 2.1.4 on 2018-12-06 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sku', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddIndex(
            model_name='attribute',
            index=models.Index(fields=['name'], name='sku_attribu_name_50cf9b_idx'),
        ),
    ]
