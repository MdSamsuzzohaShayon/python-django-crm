# Generated by Django 3.1.1 on 2020-09-22 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200922_0914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date_created',
        ),
        migrations.AddField(
            model_name='product',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]