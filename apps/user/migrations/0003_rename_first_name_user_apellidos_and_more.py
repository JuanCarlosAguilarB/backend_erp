# Generated by Django 4.0 on 2024-01-07 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0002_remove_user_country_remove_user_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='status',
            new_name='estatus',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='nombres',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phone',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='user',
            name='area',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='cargo',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
