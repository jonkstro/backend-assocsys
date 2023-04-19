# Generated by Django 4.2 on 2023-04-18 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('associado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carteira', models.ImageField(upload_to='carteiras')),
                ('associado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associado.associado')),
            ],
        ),
    ]