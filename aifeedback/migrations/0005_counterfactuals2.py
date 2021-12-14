# Generated by Django 3.1.4 on 2021-03-10 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aifeedback', '0004_instances2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counterfactuals2',
            fields=[
                ('Counterfactualid', models.AutoField(primary_key=True, serialize=False)),
                ('c_charge_degree', models.CharField(max_length=20)),
                ('race', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('priors_count', models.IntegerField()),
                ('recidivism', models.BooleanField()),
                ('unfair', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=None, null=True)),
                ('instanceid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aifeedback.instances2')),
            ],
        ),
    ]