# Generated by Django 4.0.1 on 2022-09-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
            },
        ),
    ]
