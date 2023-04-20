# Generated by Django 4.1.7 on 2023-04-20 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('descricao', models.TextField()),
                ('prazo', models.DateField(blank=True)),
                ('documento', models.FileField(blank=True, upload_to='documentos')),
            ],
        ),
    ]
