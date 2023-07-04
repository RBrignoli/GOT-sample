# Generated by Django 4.2.3 on 2023-07-04 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('is_alive', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('seasons', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('animal', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=100)),
                ('year_of_foundation', models.PositiveIntegerField()),
                ('number_of_members', models.PositiveIntegerField()),
                ('motto', models.CharField(max_length=100)),
                ('ancestral_weapon', models.CharField(max_length=100)),
                ('lady', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='houses_lady', to='gotapi.character')),
                ('lord', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='houses_lord', to='gotapi.character')),
            ],
        ),
    ]