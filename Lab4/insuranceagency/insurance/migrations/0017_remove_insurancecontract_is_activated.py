# Generated by Django 4.2.5 on 2023-09-29 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0016_alter_insuranceagent_ins_branch_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insurancecontract',
            name='is_activated',
        ),
    ]
