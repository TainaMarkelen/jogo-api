# Generated by Django 3.2.8 on 2021-11-01 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personagens', '0012_nome_profissoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nome',
            name='profissoes',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='personagens.profissoes'),
        ),
    ]
