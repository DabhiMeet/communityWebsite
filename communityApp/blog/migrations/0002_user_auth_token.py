# Generated by Django 3.1.4 on 2021-01-01 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_token',
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
    ]
