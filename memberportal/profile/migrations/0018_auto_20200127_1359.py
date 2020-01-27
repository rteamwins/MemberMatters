# Generated by Django 3.0.2 on 2020-01-27 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0017_auto_20200127_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='last_memberbucks_purchase',
            new_name='last_memberbucks_purchase',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='memberbucks_balance',
            new_name='memberbucks_balance',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='can_see_members_memberbucks',
        ),
        migrations.AddField(
            model_name='profile',
            name='can_see_members_memberbucks',
            field=models.BooleanField(default=False, verbose_name='Can see member memberbucks details'),
        ),
    ]
