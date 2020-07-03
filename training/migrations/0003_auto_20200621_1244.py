# Generated by Django 3.0.4 on 2020-06-21 12:44

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_auto_20200311_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'beach'), (2, 'hiking'), (3, 'mountain'), (4, 'test')], max_length=3, null=True),
        ),
    ]
