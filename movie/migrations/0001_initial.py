# Generated by Django 2.0.13 on 2019-03-23 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(default='Not provided')),
                ('year', models.IntegerField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('genre', models.ManyToManyField(to='movie.Genre')),
            ],
        ),
    ]