# Generated by Django 3.0 on 2021-01-25 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('pwd', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_q', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=15)),
                ('gdate', models.DateField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.user_reg')),
            ],
        ),
    ]