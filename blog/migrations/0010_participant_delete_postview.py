# Generated by Django 4.2.9 on 2024-03-17 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_postview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('team', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='PostView',
        ),
    ]