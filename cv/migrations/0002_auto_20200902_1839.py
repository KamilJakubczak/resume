# Generated by Django 3.0.10 on 2020-09-02 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='compoany_logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/cv/jobs/'),
        ),
        migrations.AlterField(
            model_name='education',
            name='school_logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/cv/education/'),
        ),
    ]
