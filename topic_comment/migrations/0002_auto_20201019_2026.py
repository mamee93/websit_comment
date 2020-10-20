# Generated by Django 3.1.2 on 2020-10-19 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topic_comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='topic_comment.comments'),
        ),
    ]