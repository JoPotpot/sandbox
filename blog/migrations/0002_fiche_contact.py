# Generated by Django 2.0.2 on 2018-03-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fiche_Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
    ]