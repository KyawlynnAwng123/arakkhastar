# Generated by Django 4.0.1 on 2022-10-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_rename_address_contact_message_contact_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, default='static/assets/img/hero-bg.jpg', null=True, upload_to='static/%Y/%m/%d/about'),
        ),
    ]
