# Generated by Django 5.0.4 on 2024-04-13 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_room_host_room_tipic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.RenameField(
            model_name='room',
            old_name='tipic',
            new_name='topic',
        ),
    ]
