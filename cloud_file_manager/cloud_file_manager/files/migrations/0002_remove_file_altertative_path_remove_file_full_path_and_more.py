# Generated by Django 4.0 on 2021-12-12 15:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='altertative_path',
        ),
        migrations.RemoveField(
            model_name='file',
            name='full_path',
        ),
        migrations.AddField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default=0, max_length=1024, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
