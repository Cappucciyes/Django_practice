# Generated by Django 4.2.3 on 2023-08-05 08:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('caacfd40-dff4-4646-b6ae-d59ab4d95fba'), editable=False, primary_key=True, serialize=False),
        ),
    ]