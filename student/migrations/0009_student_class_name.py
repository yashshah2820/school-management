# Generated by Django 3.0.5 on 2020-06-26 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0007_delete_fee'),
        ('student', '0008_auto_20200625_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_name',
            field=models.ForeignKey(default=1201, on_delete=django.db.models.deletion.CASCADE, to='administration.Class'),
            preserve_default=False,
        ),
    ]