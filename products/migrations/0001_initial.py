# Generated by Django 3.2.7 on 2021-09-01 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
