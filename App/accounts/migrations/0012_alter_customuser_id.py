# Generated by Django 4.2.3 on 2023-08-05 08:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('438c7b36-9225-4b4e-8b9d-4327afedf681'), editable=False, primary_key=True, serialize=False),
        ),
    ]
