# Generated by Django 3.1.4 on 2021-03-28 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blognation', '0005_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='username',
            new_name='name2',
        ),
    ]