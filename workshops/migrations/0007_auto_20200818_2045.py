# Generated by Django 3.0.7 on 2020-08-18 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0006_auto_20200818_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='order',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name="Add 'order-md-first' or 'order-md-last' accordingly*"),
        ),
    ]