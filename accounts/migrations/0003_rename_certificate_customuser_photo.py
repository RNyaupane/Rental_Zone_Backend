# Generated by Django 3.2.13 on 2022-07-31 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_certificate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='certificate',
            new_name='photo',
        ),
    ]
