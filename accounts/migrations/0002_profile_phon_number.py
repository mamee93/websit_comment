# Generated by Django 3.1.2 on 2020-10-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phon_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
