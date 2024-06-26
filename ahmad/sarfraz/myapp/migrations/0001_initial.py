# Generated by Django 5.0.2 on 2024-05-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=10)),
                ('father_name', models.CharField(max_length=20)),
                ('father_occupation', models.CharField(max_length=10, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('matric_school_name', models.TextField(max_length=30)),
                ('matric_marks', models.CharField(max_length=10)),
                ('matric_roll_number', models.CharField(max_length=10)),
                ('matric_board', models.CharField(max_length=20)),
                ('inter_college_name', models.CharField(max_length=40)),
                ('inter_marks', models.CharField(max_length=20)),
                ('inter_roll_number', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='admissions')),
                ('Gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Car_parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('registration_number', models.CharField(max_length=20)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('vehicle_type', models.CharField(max_length=20)),
                ('upload_paid_challan_pic', models.ImageField(upload_to='parking')),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('registration_number', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('monthly_income', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('fee_challan', models.ImageField(upload_to='fee_concession')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=20)),
                ('registration_number', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('department', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Repeat_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('email', models.EmailField(max_length=40)),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='Repeat_course')),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='scholarship')),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('roll_number', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=20)),
                ('monthly_income', models.CharField(max_length=20)),
                ('gardian_profession', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10)),
                ('father_name', models.CharField(default='', max_length=20)),
                ('phone_number', models.CharField(max_length=11)),
                ('email_address', models.EmailField(default='', max_length=20)),
                ('password', models.CharField(default='', max_length=20)),
                ('cnic', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email_address', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('cnic', models.CharField(max_length=20)),
            ],
        ),
    ]
