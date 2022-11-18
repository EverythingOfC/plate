# Generated by Django 4.1.3 on 2022-11-18 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('a_name', models.CharField(max_length=15, verbose_name='관리자')),
                ('a_id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='아이디')),
                ('a_pw', models.CharField(max_length=15, verbose_name='비밀번호')),
                ('a_de', models.IntegerField(default=0, verbose_name='검출한 수')),
                ('a_wh', models.IntegerField(default=0, verbose_name='보류한 수')),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_tel', models.CharField(max_length=15, unique=True, verbose_name='연락처')),
                ('c_name', models.CharField(max_length=15, verbose_name='차주')),
                ('c_count', models.IntegerField(default=0, verbose_name='단속횟수')),
                ('c_addr', models.TextField(verbose_name='거주지')),
                ('c_date', models.DateTimeField(blank=True, null=True, verbose_name='단속일자')),
            ],
            options={
                'db_table': 'Citizen',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_num', models.CharField(max_length=15, unique=True, verbose_name='번호판')),
                ('car_image', models.ImageField(default='default.jpg', unique=True, upload_to='images/')),
                ('car_check', models.IntegerField(default=0, verbose_name='검출 유무')),
                ('car_accur', models.FloatField(default=0.0, verbose_name='정확도')),
                ('citizen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plate.citizen')),
            ],
            options={
                'db_table': 'Car',
            },
        ),
    ]
