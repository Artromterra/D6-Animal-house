# Generated by Django 2.2.6 on 2020-01-06 11:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Кличка')),
                ('breed', models.CharField(max_length=50, verbose_name='Порода')),
                ('description', models.TextField()),
                ('age', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(50)], verbose_name='Возраст')),
                ('date_of_receipt', models.DateTimeField(auto_now=True, verbose_name='Дата поступления')),
                ('image', models.ImageField(blank=True, upload_to='pets_photo')),
                ('type_of_animal', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='animal_data.TypeOfAnimal')),
            ],
        ),
    ]
