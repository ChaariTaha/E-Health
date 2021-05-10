# Generated by Django 3.0.5 on 2021-05-10 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aboutPatient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analyste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('motDePasse', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('dateDeNaissance', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Docteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('motDePasse', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('dateDeNaissance', models.DateField()),
                ('specialite', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pharmacien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('motDePasse', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('dateDeNaissance', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Radiologue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('motDePasse', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('dateDeNaissance', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('motDePasse', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('dateDeNaissance', models.DateField()),
                ('idDossier', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aboutPatient.Dossier')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
