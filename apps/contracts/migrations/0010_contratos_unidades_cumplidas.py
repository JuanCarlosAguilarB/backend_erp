# Generated by Django 4.0 on 2024-02-10 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0009_contratos_cantidad_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratos',
            name='unidades_cumplidas',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]