# Generated by Django 4.2.20 on 2025-04-24 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technical_analysis_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('company_name', models.CharField(max_length=100)),
            ],
        ),
    ]
