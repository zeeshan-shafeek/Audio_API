# Generated by Django 4.2.1 on 2023-05-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AudioIntelligenceAPI', '0003_useraudio_class_distribution_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraudio',
            name='solution_audio',
            field=models.CharField(blank=True, default=None, null=True),
        ),
    ]