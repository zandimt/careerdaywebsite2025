# Generated by Django 5.2 on 2025-04-12 10:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_sessionregistration_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('body_html', models.TextField(help_text='Supports HTML.')),
            ],
        ),
    ]
