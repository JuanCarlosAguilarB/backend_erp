# Generated by Django 4.0 on 2024-01-08 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0006_delete_personal'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordendetrabajo',
            name='genero',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
    ]
