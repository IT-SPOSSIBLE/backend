# Generated by Django 5.1.7 on 2025-05-13 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MotocycleImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imageUrl', models.URLField()),
                ('is_primary', models.BooleanField(default=False)),
                ('uploaded_at', models.DateTimeField()),
            ],
        ),
    ]
