# Generated by Django 4.0.2 on 2022-02-28 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0005_contactform_delete_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='alias',
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('img1', models.FileField(upload_to='')),
                ('img2', models.FileField(upload_to='')),
                ('img3', models.FileField(upload_to='')),
                ('tagLine', models.CharField(blank=True, max_length=128, null=True)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('is_avail', models.BooleanField(default=True)),
                ('date_added', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('subCat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.subcategory')),
            ],
        ),
    ]
