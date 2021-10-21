# Generated by Django 3.2.4 on 2021-10-20 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20211020_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='membership_plan',
        ),
        migrations.AddField(
            model_name='membership',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]
