# Generated by Django 4.2.1 on 2023-06-28 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_name_customer_first_name_customer_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
    ]
