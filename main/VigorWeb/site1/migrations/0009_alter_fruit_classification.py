# Generated by Django 5.0.4 on 2024-05-14 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0008_alter_fruit_classification_alter_fruit_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='classification',
            field=models.CharField(choices=[('HIGH_CALORIES', 'nhiều calo'), ('LOW_CALORIES', 'ít calo'), ('MODERATE_CALORIES', 'calo vừa phải')], max_length=50),
        ),
    ]
