# Generated by Django 3.1.2 on 2020-10-31 14:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Spaceship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('ship_class', models.CharField(choices=[('W', 'Warrior'), ('P', 'Pirate'), ('M', 'Merchant'), ('D', 'Diplomat')], default='W', max_length=1, verbose_name='Spaceship class')),
                ('speed', models.IntegerField(default=100, help_text='Spaceship speed', verbose_name='Speed')),
                ('current_hp', models.IntegerField(default=0, help_text='Spaceship Hit Points', validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Hit Points')),
                ('max_hp', models.IntegerField(default=1, help_text='Spaceship Hit Points', verbose_name='Hit Points')),
                ('max_distance', models.IntegerField(default=1, help_text='Spaceship Max Distance for Hyper-jump', verbose_name='Max Distance')),
                ('pilot', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='space_rangers.pilot')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PilotFraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space_rangers.fraction')),
                ('pilot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space_rangers.pilot')),
            ],
            options={
                'unique_together': {('pilot', 'fraction')},
            },
        ),
        migrations.AddField(
            model_name='pilot',
            name='fractions',
            field=models.ManyToManyField(related_name='pilots', related_query_name='all_pilots', through='space_rangers.PilotFraction', to='space_rangers.Fraction'),
        ),
        migrations.AddField(
            model_name='pilot',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pilots', to='space_rangers.race'),
        ),
    ]
