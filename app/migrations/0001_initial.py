# Generated by Django 3.2.4 on 2022-01-27 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('user_id', models.IntegerField()),
                ('password', models.CharField(max_length=70)),
            ],
        ),
    ]
