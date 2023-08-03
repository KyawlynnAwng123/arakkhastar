# Generated by Django 4.0.1 on 2022-10-03 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_post_slug_alter_post_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='address',
            new_name='Message',
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]