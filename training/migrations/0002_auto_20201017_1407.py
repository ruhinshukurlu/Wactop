# Generated by Django 3.0.4 on 2020-10-17 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0004_auto_20201017_1114'),
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='training',
            old_name='adress',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='training',
            name='training_type',
        ),
        migrations.AddField(
            model_name='training',
            name='training_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='training', to='tour.TourType'),
            preserve_default=False,
        ),
    ]