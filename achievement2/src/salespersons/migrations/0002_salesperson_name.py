# Generated by Django 4.2.2 on 2023-06-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salespersons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesperson',
            name='name',
            field=models.CharField(default='no name', max_length=120),
        ),
    ]
