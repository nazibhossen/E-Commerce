# Generated by Django 4.2.1 on 2023-07-01 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_customer_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
