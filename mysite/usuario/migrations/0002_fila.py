# Generated by Django 2.0.1 on 2018-07-25 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fila',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('agencia', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=150)),
                ('fecha', models.CharField(max_length=150)),
                ('total', models.IntegerField()),
            ],
        ),
    ]