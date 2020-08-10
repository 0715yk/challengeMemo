# Generated by Django 3.0.5 on 2020-04-06 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habbit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habbitName', models.CharField(max_length=13)),
                ('startDate', models.CharField(max_length=30)),
                ('progress', models.CharField(max_length=66)),
                ('finishDate', models.CharField(max_length=30)),
                ('daysCount', models.SmallIntegerField()),
                ('daysFail', models.SmallIntegerField()),
                ('daysSucceed', models.SmallIntegerField()),
                ('give_up', models.BooleanField(default=False)),
                ('givenup_date', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField()),
                ('habbit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='memoApp.Habbit')),
            ],
        ),
    ]
