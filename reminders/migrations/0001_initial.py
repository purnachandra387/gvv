# Generated by Django 5.1.4 on 2024-12-05 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garden', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(choices=[('watering', 'Watering'), ('fertilizing', 'Fertilizing'), ('pruning', 'Pruning'), ('other', 'Other')], max_length=50)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('is_completed', models.BooleanField(default=False)),
                ('garden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden.garden')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden.plant')),
            ],
        ),
    ]
