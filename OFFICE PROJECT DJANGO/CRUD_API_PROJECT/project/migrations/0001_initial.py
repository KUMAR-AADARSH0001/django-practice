# Generated by Django 4.1.5 on 2023-02-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField()),
                ('stream', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('join_at', models.DateTimeField()),
            ],
        ),
    ]
