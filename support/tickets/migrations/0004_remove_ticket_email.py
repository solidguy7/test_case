# Generated by Django 4.1.6 on 2023-02-14 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_ticket_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='email',
        ),
    ]
