# Generated by Django 2.2b1 on 2019-03-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190311_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uri',
            field=models.URLField(null=True),
        ),
    ]
