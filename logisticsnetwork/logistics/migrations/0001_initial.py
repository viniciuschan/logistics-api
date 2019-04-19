# Generated by Django 2.1.8 on 2019-04-19 01:55

from decimal import Decimal
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogisticsNet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('path_data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('state', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='state')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='date added')),
            ],
            options={
                'verbose_name': 'Logistic Network',
            },
        ),
        migrations.CreateModel(
            name='UserSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=20, verbose_name='source')),
                ('destination', models.CharField(max_length=20, verbose_name='destination')),
                ('autonomy', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=4, verbose_name='\x1cautonomy')),
                ('fuel_price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=4, verbose_name='fuel_price')),
            ],
            options={
                'verbose_name': 'User',
            },
        ),
    ]