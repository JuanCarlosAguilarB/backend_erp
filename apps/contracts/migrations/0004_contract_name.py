# Generated by Django 4.2 on 2023-09-11 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_alter_contract_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
