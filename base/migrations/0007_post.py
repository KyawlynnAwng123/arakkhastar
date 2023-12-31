# Generated by Django 4.0.1 on 2022-09-30 04:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0006_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('short_content', models.TextField()),
                ('long_content', models.TextField()),
                ('show_image', models.BooleanField(default=True)),
                ('views', models.IntegerField()),
                ('category', models.ForeignKey(default='Arakkhastar', on_delete=django.db.models.deletion.CASCADE, to='base.category')),
                ('tags', models.ManyToManyField(to='base.Tag')),
                ('user', models.ForeignKey(default='Admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
