# Generated by Django 5.0.7 on 2024-08-06 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0010_auto_20210723_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('due_date', models.DateField()),
                ('category', models.CharField(max_length=50)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium', max_length=6)),
                ('progress', models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Not Started', max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2024-08-06'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2024-08-06'),
        ),
    ]
