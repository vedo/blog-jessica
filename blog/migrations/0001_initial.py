# Generated by Django 3.0.4 on 2020-03-23 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateTimeField()),
                ('autor', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='')),
                ('contenido', models.TextField()),
                ('tags', models.ManyToManyField(to='blog.Tag')),
            ],
        ),
    ]
