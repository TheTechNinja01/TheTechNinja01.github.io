# Generated by Django 3.2.5 on 2023-05-22 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetImage',
            fields=[
                ('ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_Name', models.CharField(max_length=255)),
                #('Folder_Location', models.CharField(max_length=100)),
                ('File', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Galleria',
            },
        ),
    ]
