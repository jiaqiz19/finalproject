# Generated by Django 3.1 on 2019-12-07 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sq',
            name='X',
            field=models.CharField(default=None, help_text='x', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='Y',
            field=models.CharField(default=None, help_text='y', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='bb',
            field=models.CharField(default=None, help_text='borough boundaries', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='ccd',
            field=models.CharField(default=None, help_text='city council districts', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='ccolor',
            field=models.CharField(default=None, help_text='combination color', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='cdistricts',
            field=models.CharField(default=None, help_text='community districts', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='cnotes',
            field=models.CharField(default=None, help_text='color notes', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='color',
            field=models.CharField(default=None, help_text='primary color', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='date',
            field=models.DateField(default=None, help_text='date'),
        ),
        migrations.AlterField(
            model_name='sq',
            name='hcolor',
            field=models.CharField(default=None, help_text='highlight fur color', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='hectare',
            field=models.CharField(default=None, help_text='hectare', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='hectarenumber',
            field=models.CharField(default=None, help_text='hectare squirrel number', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='ll',
            field=models.CharField(default=None, help_text='lat/long', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='location',
            field=models.CharField(default=None, help_text='location', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='measurement',
            field=models.CharField(default=None, help_text='measurement', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='otheract',
            field=models.CharField(default=None, help_text='other activities', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='otherinter',
            field=models.CharField(default=None, help_text='other interactions', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='pp',
            field=models.CharField(default=None, help_text='police precincts', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='slocation',
            field=models.CharField(default=None, help_text='specific location', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='zc',
            field=models.CharField(default=None, help_text='zip codes', max_length=100),
        ),
    ]