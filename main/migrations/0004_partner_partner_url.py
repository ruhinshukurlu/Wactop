# Generated by Django 3.0.4 on 2020-11-16 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201115_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='partner_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Partner Link'),
        ),
    ]
