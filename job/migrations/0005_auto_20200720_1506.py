# Generated by Django 3.0.8 on 2020-07-20 13:06

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20200720_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to=job.models.image_upload),
        ),
    ]
