# Generated by Django 3.2 on 2021-04-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('description', models.TextField(max_length=250)),
                ('email', models.TextField(max_length=24)),
                ('startDate', models.DateField(max_length=2)),
                ('endDate', models.DateField(max_length=2)),
            ],
        ),
    ]