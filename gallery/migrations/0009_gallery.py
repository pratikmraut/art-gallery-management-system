# Generated by Django 3.1.2 on 2020-10-26 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_painting_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_id', models.IntegerField()),
                ('g_name', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.artists')),
            ],
        ),
    ]
