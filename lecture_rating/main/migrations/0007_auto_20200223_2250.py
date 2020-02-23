# Generated by Django 3.0.3 on 2020-02-23 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_auto_20200223_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectureratingboard',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecture_id',
            field=models.CharField(default='TUPOIJEL', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
