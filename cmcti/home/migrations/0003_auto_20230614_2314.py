# Generated by Django 3.0 on 2023-06-15 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_demanda_criado_por'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demanda',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to='documentos'),
        ),
    ]