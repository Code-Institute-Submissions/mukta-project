# Generated by Django 3.0.7 on 2020-08-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True)),
                ('location', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=10)),
                ('instructor', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('images', models.URLField(blank=True, max_length=1024, null=True)),
            ],
        ),
    ]
