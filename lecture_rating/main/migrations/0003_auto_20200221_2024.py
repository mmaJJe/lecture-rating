# Generated by Django 2.2.3 on 2020-02-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200221_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture_id',
            field=models.CharField(default='CX0T7Z42', max_length=20, primary_key=True, serialize=False),
        ),
    ]
