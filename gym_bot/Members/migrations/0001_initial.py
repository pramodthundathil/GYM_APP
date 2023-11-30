# Generated by Django 3.2.14 on 2023-11-29 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batch_Name', models.CharField(choices=[('Morning', 'Morning'), ('After Noon', 'After Noon'), ('Evening', 'Evening'), ('Stoped', 'Stoped')], max_length=255)),
                ('Batch_Status', models.BooleanField(default=True)),
                ('Batch_Time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MemberData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=255)),
                ('Last_Name', models.CharField(max_length=255)),
                ('Date_Of_Birth', models.DateField()),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=255)),
                ('Mobile_Number', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.TextField(max_length=200)),
                ('Medical_History', models.TextField(blank=True, max_length=2000, null=True)),
                ('Registration_Date', models.DateField()),
                ('Photo', models.FileField(upload_to='member_photo')),
                ('Active_status', models.BooleanField(default=True)),
                ('Access_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_Of_Subscription', models.CharField(max_length=255)),
                ('Amount', models.IntegerField()),
                ('Subscribed_Date', models.DateField()),
                ('Batch_Status', models.BooleanField(default=True)),
                ('Payment_Status', models.BooleanField(default=False)),
                ('Batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Members.batch_db')),
                ('Member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Members.memberdata')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField()),
                ('Payment_Status', models.BooleanField(default=True)),
                ('Access_status', models.BooleanField(default=False)),
                ('Member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Members.memberdata')),
                ('Subscription_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Members.subscription')),
            ],
        ),
    ]