# Generated by Django 4.0.6 on 2022-07-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proprietario', '0003_remove_proprietario_carros'),
    ]

    operations = [
        migrations.AddField(
            model_name='proprietario',
            name='totalCarros',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]