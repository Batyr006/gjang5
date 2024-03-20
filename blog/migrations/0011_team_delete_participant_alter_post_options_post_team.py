# Generated by Django 4.2.9 on 2024-03-18 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_participant_delete_postview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название команды')),
                ('description', models.TextField(verbose_name='Описание команды')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.AddField(
            model_name='post',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.team', verbose_name='Команда'),
            preserve_default=False,
        ),
    ]
