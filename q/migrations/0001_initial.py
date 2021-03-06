# Generated by Django 4.0.2 on 2022-03-02 19:23

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('desc', models.CharField(max_length=4141)),
            ],
        ),
        migrations.CreateModel(
            name='Register_Model',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('reemail', models.EmailField(max_length=254)),
                ('repassword', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('city', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=250)),
                ('image', models.ImageField(upload_to='imgs/')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='q.category')),
            ],
        ),
    ]
