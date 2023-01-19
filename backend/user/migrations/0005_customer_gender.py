# Generated by Django 4.1.5 on 2023-01-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_customer_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[['male', 'Male'], ['female', 'Female'], ['other', 'Other']], default='male', max_length=20),
            preserve_default=False,
        ),
    ]