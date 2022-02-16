# Generated by Django 4.0.2 on 2022-02-16 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chores', '0006_remove_chore_assignee_chore_assignees'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('sended_at', models.DateTimeField(auto_now_add=True)),
                ('_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favor_sended', related_query_name='favor_sended', to=settings.AUTH_USER_MODEL)),
                ('chore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favor', related_query_name='favor', to='chores.chore')),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favor_received', related_query_name='favor_received', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
