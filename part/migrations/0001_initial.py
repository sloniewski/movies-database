# Generated by Django 2.0.13 on 2019-03-23 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(max_length=32)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cast', to='movie.Movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cast_member', to='person.Person')),
            ],
            options={
                'verbose_name_plural': 'Cast',
            },
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=32, null=True)),
                ('credit', models.CharField(blank=True, max_length=32, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='crew', to='movie.Movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='crew_member', to='person.Person')),
            ],
            options={
                'verbose_name_plural': 'Crew',
            },
        ),
    ]
