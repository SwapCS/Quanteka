# Generated by Django 4.0.5 on 2022-09-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantekaapp', '0004_alter_report_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='category',
        ),
        migrations.AddField(
            model_name='report',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='reports', to='quantekaapp.reportcategory'),
        ),
    ]
