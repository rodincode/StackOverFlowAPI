# Generated by Django 3.1.4 on 2021-04-09 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20210409_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='order',
            field=models.CharField(blank=True, choices=[('1', 'activity'), ('2', 'votes'), ('3', 'creation'), ('3', 'relevance')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='sort',
            field=models.CharField(blank=True, choices=[('1', 'desc'), ('2', 'asc')], default=None, max_length=30, null=True),
        ),
    ]
