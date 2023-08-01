# Generated by Django 4.2.3 on 2023-08-01 07:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('77de2a9b-0c2b-4858-a616-27ec3541e0a9'), editable=False, primary_key=True, serialize=False),
        ),
    ]
