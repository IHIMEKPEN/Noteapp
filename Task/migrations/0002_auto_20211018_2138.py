# Generated by Django 3.2.8 on 2021-10-18 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='note',
            field=models.TextField(max_length=2000),
        ),
    ]
