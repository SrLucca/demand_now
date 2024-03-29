# Generated by Django 4.1.12 on 2023-10-16 02:37

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
                ('tipo', models.CharField(choices=[('Demanda', 'Demanda'), ('Documento', 'Documento')], max_length=50)),
                ('descricao', models.TextField()),
                ('prazo', models.DateField(blank=True, null=True)),
                ('documento', models.FileField(blank=True, null=True, upload_to='documentos')),
                ('concluida', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
