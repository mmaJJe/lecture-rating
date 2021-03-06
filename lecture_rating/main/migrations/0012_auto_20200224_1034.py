# Generated by Django 3.0.3 on 2020-02-24 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_merge_20200224_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture_id',
            field=models.CharField(default='7HBHUHQ3', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=25)),
                ('admission_year', models.CharField(default=0, max_length=4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
