# Generated by Django 5.1.1 on 2024-11-02 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_doctormodel_hospitalmodel_delete_doctorinfo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalmodel',
            name='doctors',
            field=models.ManyToManyField(blank=True, related_name='hospitals', to='hospital.doctormodel'),
        ),
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('token_number', models.PositiveIntegerField(editable=False, unique=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctormodel')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospitalmodel')),
            ],
        ),
    ]
