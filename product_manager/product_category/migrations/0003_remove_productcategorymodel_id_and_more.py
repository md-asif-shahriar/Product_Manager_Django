# Generated by Django 4.2.4 on 2023-09-03 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_category', '0002_alter_productcategorymodel_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategorymodel',
            name='id',
        ),
        migrations.AddField(
            model_name='productcategorymodel',
            name='cid',
            field=models.IntegerField(default='21488', editable=False, primary_key=True, serialize=False),
        ),
    ]
