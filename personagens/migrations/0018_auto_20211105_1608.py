# Generated by Django 3.2.8 on 2021-11-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personagens', '0017_rename_nome_personagens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modificadores',
            name='ataque',
            field=models.IntegerField(verbose_name='Ataque'),
        ),
        migrations.AlterField(
            model_name='modificadores',
            name='velocidade',
            field=models.IntegerField(verbose_name='Velocidade'),
        ),
    ]
