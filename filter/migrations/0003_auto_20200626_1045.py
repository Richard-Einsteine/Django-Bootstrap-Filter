# Generated by Django 2.2.2 on 2020-06-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0002_auto_20200626_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
