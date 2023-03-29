# Generated by Django 2.1.5 on 2019-03-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('minimal', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='greeting',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]