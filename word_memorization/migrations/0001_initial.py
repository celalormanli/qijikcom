# Generated by Django 3.1.4 on 2021-01-17 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(default=100, max_length=100)),
                ('turkish', models.CharField(default=100, max_length=100)),
                ('german', models.CharField(default=100, max_length=100)),
                ('french', models.CharField(default=100, max_length=100)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='word_memorization.category')),
            ],
        ),
    ]
