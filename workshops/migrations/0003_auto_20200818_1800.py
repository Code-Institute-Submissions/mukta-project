# Generated by Django 3.0.7 on 2020-08-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0002_auto_20200808_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='order',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name="'order-first' or 'order-last'*"),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='date',
            field=models.DateField(blank=True, verbose_name='Date YYYY-MM-DD*'),
        ),
    ]