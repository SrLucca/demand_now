# Generated by Django 4.1.7 on 2023-05-30 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demanda',
            name='prazo',
            field=models.DateField(blank=True, null=True),
        ),
    ]