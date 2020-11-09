# Generated by Django 3.0.4 on 2020-11-09 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizer', '0001_initial'),
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('keyword', models.CharField(blank=True, max_length=255, null=True)),
                ('descriptionaz', models.TextField(blank=True, null=True)),
                ('descriptionen', models.TextField(blank=True, null=True)),
                ('descriptionru', models.TextField(blank=True, null=True)),
                ('country', models.CharField(default='Azerbaijan', max_length=31)),
                ('city', models.CharField(blank=True, max_length=31, null=True)),
                ('address', models.CharField(blank=True, max_length=63, null=True)),
                ('price', models.IntegerField()),
                ('pricefor', models.IntegerField(default=1)),
                ('currency', models.CharField(choices=[('AZN', 'AZN'), ('USD', 'USD'), ('EUR', 'EUR'), ('TRY', 'TRY'), ('RUB', 'RUB')], default='AZN', max_length=31)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('distance', models.CharField(blank=True, max_length=31, null=True)),
                ('durationday', models.IntegerField(blank=True, null=True)),
                ('durationnight', models.IntegerField(blank=True, null=True)),
                ('datefrom', models.DateField(blank=True, null=True)),
                ('dateto', models.DateField(blank=True, null=True)),
                ('viewcount', models.IntegerField(default=0)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='activity/avatar/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='activity/cover/')),
                ('guide', models.CharField(blank=True, max_length=31, null=True)),
                ('availabledays', models.CharField(blank=True, max_length=31, null=True)),
                ('status', models.IntegerField(choices=[(1, 'publish'), (2, 'draft'), (3, 'past')], default=1)),
                ('map_link', models.URLField(blank=True, max_length=300, null=True, verbose_name='Map Link')),
                ('activity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='tour.TourType')),
                ('organizer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizer.Organizer')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='ActivitySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='activity/schedule/')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='activity/image/')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityDetailRU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=31)),
                ('text', models.TextField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityDetailEN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=31)),
                ('text', models.TextField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityDetailAZ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=31)),
                ('text', models.TextField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
            ],
        ),
    ]
