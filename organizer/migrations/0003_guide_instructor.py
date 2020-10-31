# Generated by Django 3.0.4 on 2020-10-18 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_auto_20201017_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('experience', models.CharField(choices=[('1 year', '1 Year'), ('2 year', '2 Year'), ('3 year', '3 Year'), ('4 year', '4 Year'), ('5+ year', '5+ Year')], max_length=50, verbose_name='Experience')),
                ('certification', models.CharField(max_length=50, verbose_name='Certification')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to='organizer.Organizer', verbose_name='Organizer')),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('experience', models.CharField(choices=[('1 year', '1 Year'), ('2 year', '2 Year'), ('3 year', '3 Year'), ('4 year', '4 Year'), ('5+ year', '5+ Year')], max_length=50, verbose_name='Experience')),
                ('certification', models.CharField(max_length=50, verbose_name='Certification')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guide', to='organizer.Organizer', verbose_name='Organizer')),
            ],
        ),
    ]