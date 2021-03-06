# Generated by Django 2.0.6 on 2019-01-19 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room_environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=64)),
                ('room', models.CharField(max_length=16)),
                ('temperature', models.FloatField(default=-1)),
                ('humidity', models.FloatField(default=-1)),
                ('ts', models.FloatField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='SBC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(default=0)),
                ('ts', models.FloatField(default=-1)),
            ],
        ),
        migrations.AddField(
            model_name='room_environment',
            name='sbc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.SBC'),
        ),
    ]
