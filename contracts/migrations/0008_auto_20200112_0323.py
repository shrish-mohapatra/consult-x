# Generated by Django 2.2.4 on 2020-01-12 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20200112_0323'),
        ('contracts', '0007_auto_20200112_0318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='skills',
        ),
        migrations.AddField(
            model_name='contract',
            name='skills',
            field=models.ManyToManyField(blank=True, to='profiles.Skill'),
        ),
    ]
