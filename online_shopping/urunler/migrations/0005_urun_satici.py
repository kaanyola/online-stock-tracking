# Generated by Django 3.2 on 2021-05-03 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0004_satici'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='satici',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='urunler.satici'),
        ),
    ]
