# Generated by Django 3.0.4 on 2020-11-15 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_sociallink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sociallink',
            name='link',
        ),
        migrations.AddField(
            model_name='sociallink',
            name='facebook_link',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Facebook Link'),
        ),
        migrations.AddField(
            model_name='sociallink',
            name='instagram_link',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Instagram Link'),
        ),
        migrations.AddField(
            model_name='sociallink',
            name='linkedin_link',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='LinkedIn Link'),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Title'),
        ),
    ]
