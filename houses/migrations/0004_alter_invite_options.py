# Generated by Django 4.0.2 on 2022-02-19 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_alter_invite_invitee_alter_invite_inviter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invite',
            options={'ordering': ['-sended_at']},
        ),
    ]