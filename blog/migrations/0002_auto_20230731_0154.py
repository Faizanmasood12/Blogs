# Generated by Django 3.2.20 on 2023-07-30 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogs',
            options={'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'Posts'},
        ),
    ]
