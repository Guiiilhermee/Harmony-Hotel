# Generated by Django 3.2.23 on 2023-12-03 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=3)),
                ('category', models.CharField(choices=[('YAC', 'AC'), ('NAC', 'NON-AC'), ('DEL', 'DELUXE'), ('KIN', 'KING'), ('QUE', 'QUEEN')], max_length=3)),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]
