# Generated by Django 2.2.7 on 2019-12-18 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_events_past_hours_hot_person_remarks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='passive_remark',
            new_name='positive_remark',
        ),
    ]
