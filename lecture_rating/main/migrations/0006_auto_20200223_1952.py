# Generated by Django 2.2.3 on 2020-02-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200223_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectureratingboard',
            name='stars',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecture_id',
            field=models.CharField(default='ZDBHFH4P', max_length=20, primary_key=True, serialize=False),
        ),
    ]