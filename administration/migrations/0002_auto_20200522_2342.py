# Generated by Django 3.0.5 on 2020-05-22 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
