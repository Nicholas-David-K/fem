# Generated by Django 4.1.3 on 2022-12-16 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0039_remove_testimony_subject_of_testimony_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimony',
            name='testimony_subject',
            field=models.CharField(max_length=150),
        ),
    ]
