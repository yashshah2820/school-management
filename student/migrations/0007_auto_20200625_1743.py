# Generated by Django 3.0.5 on 2020-06-25 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_auto_20200625_1654'),
        ('student', '0006_assignmentanswer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AssignmentAnswer',
            new_name='Answer',
        ),
    ]