# Generated by Django 3.1.7 on 2021-05-17 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210509_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=100)),
            ],
        ),
    ]