# Generated by Django 3.0.4 on 2021-03-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0013_auto_20210309_2023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourdetailaz',
            old_name='text_az_az',
            new_name='text_en',
        ),
        migrations.RenameField(
            model_name='tourdetailaz',
            old_name='text_az_en',
            new_name='text_ru',
        ),
        migrations.RenameField(
            model_name='tourdetailaz',
            old_name='title_az_az',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='tourdetailaz',
            old_name='title_az_en',
            new_name='title_ru',
        ),
        migrations.RemoveField(
            model_name='tourdetailaz',
            name='text_az_ru',
        ),
        migrations.RemoveField(
            model_name='tourdetailaz',
            name='title_az_ru',
        ),
        migrations.AddField(
            model_name='tourdetailaz',
            name='text',
            field=models.TextField(default='text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tourdetailaz',
            name='title',
            field=models.CharField(default=2, max_length=31),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tourdetailaz',
            name='text_az',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tourdetailaz',
            name='title_az',
            field=models.CharField(max_length=31, null=True),
        ),
    ]
