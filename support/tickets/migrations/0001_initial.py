# Generated by Django 4.1.6 on 2023-02-14 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('answer', models.TextField()),
                ('status', models.CharField(choices=[('Resolved', 'Resolved'), ('Unresolved', 'Unresolved'), ('Frozen', 'Frozen')], default='Unresolved', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddIndex(
            model_name='ticket',
            index=models.Index(fields=['-created'], name='tickets_tic_created_44ae51_idx'),
        ),
    ]