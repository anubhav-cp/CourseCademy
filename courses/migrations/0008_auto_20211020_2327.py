# Generated by Django 3.2.4 on 2021-10-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20211020_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='membership_plan',
            field=models.ManyToManyField(to='courses.Membership'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('free', 'Free'), ('premium', 'Premium')], default='free', max_length=20),
        ),
    ]
