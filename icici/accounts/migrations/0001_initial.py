# Generated by Django 4.0.5 on 2022-07-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='current',
            fields=[
                ('ac_no', models.BigIntegerField(primary_key=True, serialize=False)),
                ('businessname', models.CharField(max_length=50)),
                ('ifsc', models.IntegerField()),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='fixed_deposit',
            fields=[
                ('ac_no', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('deposit_date', models.DateField()),
                ('maturity_date', models.DateField()),
                ('interest', models.IntegerField()),
                ('maturity_ammount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='saving',
            fields=[
                ('ac_no', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('ifsc', models.IntegerField()),
                ('balance', models.IntegerField()),
            ],
        ),
    ]
