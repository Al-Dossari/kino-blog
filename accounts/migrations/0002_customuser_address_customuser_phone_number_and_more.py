# Generated by Django 4.2.5 on 2023-09-18 16:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/profile_photo'),
        ),
    ]
