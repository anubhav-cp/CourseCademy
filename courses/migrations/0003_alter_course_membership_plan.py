# Generated by Django 3.2.8 on 2021-10-14 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20211014_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='membership_plan',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.membership'),
        ),
    ]
