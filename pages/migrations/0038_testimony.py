# Generated by Django 4.1.3 on 2022-12-16 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0037_alter_about_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('subject_of_testimony', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('testimony', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
