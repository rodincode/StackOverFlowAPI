# Generated by Django 3.1.4 on 2021-04-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20210409_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='order',
            field=models.CharField(blank=True, choices=[('activity', 'activity'), ('votes', 'votes'), ('creation', 'creation'), ('relevance', 'relevance')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='sort',
            field=models.CharField(blank=True, choices=[('desc', 'desc'), ('asc', 'asc')], default=None, max_length=30, null=True),
        ),
    ]
