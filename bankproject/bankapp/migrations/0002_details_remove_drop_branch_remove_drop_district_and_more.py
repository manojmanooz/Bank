# Generated by Django 4.1 on 2022-08-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('male', models.BooleanField(default=False)),
                ('female', models.BooleanField(default=False)),
                ('district', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('credit', models.BooleanField(default=False)),
                ('debit', models.BooleanField(default=False)),
                ('cheque', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='drop',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='drop',
            name='district',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='Drop',
        ),
    ]
