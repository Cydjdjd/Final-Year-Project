# Generated by Django 4.2.13 on 2024-08-20 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='careerCoachingApplicationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realName', models.CharField(blank=True, max_length=30, null=True)),
                ('emailAddress', models.CharField(blank=True, max_length=30, null=True)),
                ('contactNumber', models.CharField(blank=True, max_length=30, null=True)),
                ('normalUserApplied', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.normaluser')),
            ],
        ),
    ]
