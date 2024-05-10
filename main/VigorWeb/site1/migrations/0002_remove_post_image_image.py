# Generated by Django 5.0.4 on 2024-05-10 21:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='post_images')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site1.post')),
            ],
        ),
    ]
