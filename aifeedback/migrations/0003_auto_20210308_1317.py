# Generated by Django 3.1.4 on 2021-03-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aifeedback', '0002_auto_20210304_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counterfactuals',
            name='unactionable',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='counterfactuals',
            name='unfair',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
    ]
