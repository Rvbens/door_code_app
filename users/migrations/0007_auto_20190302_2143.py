# Generated by Django 2.1.7 on 2019-03-02 21:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('users', '0006_usuario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='CustomUser',
        ),
    ]
