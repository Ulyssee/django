# Generated by Django 3.0.5 on 2023-02-11 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0009_auto_20221212_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupeLecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('membres', models.ManyToManyField(related_name='groupes_lecture_rejoins', to=settings.AUTH_USER_MODEL)),
                ('proprietaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('heure', models.TimeField()),
                ('lieu', models.CharField(max_length=100)),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.GroupeLecture')),
            ],
        ),
    ]
