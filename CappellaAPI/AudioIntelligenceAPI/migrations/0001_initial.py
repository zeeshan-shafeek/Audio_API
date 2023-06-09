# Generated by Django 4.2.1 on 2023-05-15 15:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStamp', models.DateTimeField()),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Audio_content', models.FileField(upload_to='audio/')),
                ('Video_content', models.CharField()),
                ('Infant_cry_class_by_model', models.CharField()),
                ('Infant_cry_class_rate', models.CharField()),
                ('Infant_cry_class_by_user', models.CharField()),
            ],
        ),
    ]
