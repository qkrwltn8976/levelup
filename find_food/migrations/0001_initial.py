# Generated by Django 2.2.7 on 2019-11-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_x', models.FloatField()),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]