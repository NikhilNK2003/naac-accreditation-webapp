# Generated by Django 5.0.6 on 2024-07-07 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criteria_1', '0002_alter_criteria_1_2_2_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria_1_2_2',
            name='course_code',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]