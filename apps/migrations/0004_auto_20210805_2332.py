# Generated by Django 3.2.2 on 2021-08-05 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20210517_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='komik',
            name='cover',
            field=models.ImageField(null=True, upload_to='cover/'),
        ),
        migrations.AddField(
            model_name='komik',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]