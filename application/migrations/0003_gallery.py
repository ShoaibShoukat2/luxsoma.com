# Generated by Django 3.2.16 on 2023-06-05 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
