# Generated by Django 4.0.6 on 2022-07-28 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(blank=True, choices=[('Amarelo', 'AMARELO'), ('Azul', 'AZUL'), ('Cinza', 'CINZA')], max_length=20)),
                ('modelo', models.CharField(blank=True, choices=[('Escotilha', 'ESCOTILHA'), ('Sedan', 'SEDAN'), ('Conversível', 'CONVERSÍVEL')], max_length=20)),
            ],
        ),
    ]