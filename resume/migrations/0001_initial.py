# Generated by Django 3.0.6 on 2020-11-17 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('field', models.CharField(max_length=50)),
                ('subscription', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]
