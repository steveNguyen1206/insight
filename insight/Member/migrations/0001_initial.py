# Generated by Django 4.2.5 on 2023-09-19 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Community', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('MetamarskID', models.CharField(max_length=255)),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('content', models.CharField(max_length=255)),
                ('community_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Community.community')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCommunity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('joined_date', models.DateField(auto_now_add=True)),
                ('community_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Community.community')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Member.myuser')),
            ],
        ),
    ]
