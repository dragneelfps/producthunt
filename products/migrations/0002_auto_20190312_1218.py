# Generated by Django 2.1.7 on 2019-03-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='body',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(default=None),
        ),
    ]