# Generated by Django 4.1.3 on 2024-06-09 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfs', '0007_remove_accepted_form_is_application_initiated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latest_job',
            name='link',
        ),
        migrations.RemoveField(
            model_name='latest_job',
            name='upload',
        ),
    ]
