# Generated by Django 3.2.2 on 2021-05-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_customuser_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='nickname',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
    ]
