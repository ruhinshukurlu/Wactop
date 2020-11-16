# Generated by Django 3.0.4 on 2020-11-12 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Text')),
                ('commented_at', models.DateField(auto_now_add=True, verbose_name='Commented at')),
                ('rating', models.IntegerField(blank=True, null=True, verbose_name='Rating')),
                ('activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_comment', to='activity.Activity', verbose_name='Activity')),
                ('comment_reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='activity.Comment', verbose_name='Comment')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_comment', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]