# Generated by Django 3.0.3 on 2020-06-11 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_line', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('state', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=255, null=True)),
                ('pin_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=256)),
                ('store_type', models.CharField(max_length=500)),
                ('open_time', models.TimeField(blank=True, null=True)),
                ('close_time', models.TimeField(blank=True, null=True)),
                ('no_of_lockers', models.IntegerField()),
                ('dimension', models.CharField(max_length=50)),
                ('no_of_working_days', models.IntegerField()),
                ('no_of_working_hours', models.IntegerField()),
                ('no_of_cctv', models.IntegerField()),
                ('exist', models.CharField(max_length=4)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration_app.Address')),
                ('partner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration_app.Partner')),
            ],
        ),
    ]
