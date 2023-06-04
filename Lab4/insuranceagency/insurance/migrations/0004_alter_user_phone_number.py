# Generated by Django 4.2.1 on 2023-06-03 17:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0003_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Телефонный номер должен быть введен в формате: '+37529xxxxxxx'. Разрешено до 15 цифр", regex='^\\+37529\\d{7}$')]),
        ),
    ]
