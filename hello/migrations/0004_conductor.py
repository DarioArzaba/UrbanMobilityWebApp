# Generated by Django 2.1.5 on 2019-03-02 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_remove_producto_when'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20)),
            ],
        ),
    ]