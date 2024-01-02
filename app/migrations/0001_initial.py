# Generated by Django 4.1.12 on 2023-12-25 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=255)),
                ('monthly_income', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='father', to='app.guardian')),
                ('guardian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guardian', to='app.guardian')),
                ('mother', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mother', to='app.guardian')),
            ],
        ),
        migrations.CreateModel(
            name='AdmissionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residential_certificate', models.FileField(upload_to='doc/')),
                ('adhaar_card', models.FileField(upload_to='doc/')),
                ('weight_of_child', models.IntegerField(null=True)),
                ('has_disability', models.BooleanField(default=False)),
                ('disability_certificate', models.FileField(blank=True, null=True, upload_to='doc/')),
                ('applied_for_disability_certificate', models.BooleanField(default=False)),
                ('medical_report', models.FileField(upload_to='doc/')),
                ('cast_certificate', models.FileField(null=True, upload_to='doc/')),
                ('taking_medicines_daily', models.BooleanField(default=False)),
                ('behaves_inappropriately', models.BooleanField(default=False)),
                ('problem_description', models.TextField(blank=True, null=True)),
                ('hears_name_when_called', models.BooleanField(default=False)),
                ('received_allowance', models.BooleanField(default=False)),
                ('enrollment_class', models.CharField(max_length=255)),
                ('bank_name', models.CharField(max_length=255)),
                ('branch_name', models.CharField(max_length=255)),
                ('ifsc_code', models.CharField(max_length=20)),
                ('account_number', models.CharField(max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]