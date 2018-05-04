# Generated by Django 2.0.4 on 2018-04-24 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180423_2027'),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('slug', models.SlugField()),
                ('job_type', models.CharField(choices=[('fulltime', 'Full-Time'), ('parttime', 'Part-Time')], max_length=10)),
                ('min_qualification', models.CharField(blank=True, choices=[('ssce', 'SSCE'), ('bsc', 'BSc'), ('msc', 'MSc'), ('phd', 'PhD')], max_length=10, null=True, verbose_name='Minimum Qualification')),
                ('years_of_exp', models.CharField(blank=True, choices=[('entry', 'Entry Level'), ('1-2', '1-2 years'), ('3-5', '3-5 years'), ('6-10', '6-10 years'), ('above 10', 'Above 10 years')], max_length=20, null=True, verbose_name='Years of Experience')),
                ('salary', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Company')),
            ],
        ),
        migrations.AlterModelOptions(
            name='industry',
            options={'verbose_name_plural': 'Industries'},
        ),
        migrations.AddField(
            model_name='job',
            name='industry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Industry'),
        ),
    ]