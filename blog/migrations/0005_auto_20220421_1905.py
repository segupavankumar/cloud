# Generated by Django 3.2.6 on 2022-04-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220421_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date_posted',
        ),
        migrations.AlterField(
            model_name='blog',
            name='img1',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='img2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
