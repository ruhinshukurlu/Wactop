# Generated by Django 3.0.4 on 2021-01-14 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0008_auto_20210114_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityDeny',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Text')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Commented at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Commented at')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deny', to='activity.Activity')),
            ],
            options={
                'verbose_name': 'ActivityDeny',
                'verbose_name_plural': 'ActivityDenies',
            },
        ),
    ]
