# Generated by Django 3.2.6 on 2021-09-23 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fo_title', models.CharField(max_length=200, verbose_name='제목')),
                ('fo_desc', models.TextField(verbose_name='내용')),
                ('fo_day', models.DateField(default=django.utils.timezone.now, verbose_name='등록일')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '게시판',
            },
        ),
    ]
