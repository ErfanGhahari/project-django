# Generated by Django 4.1 on 2022-09-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='free_consulation',
            name='data_create',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='free_consulation',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
    ]
