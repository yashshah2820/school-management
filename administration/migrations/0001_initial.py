# Generated by Django 3.0.5 on 2020-05-02 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher')),
            ],
        ),
    ]
