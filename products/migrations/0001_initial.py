# Generated by Django 2.1.7 on 2019-03-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('uon', models.CharField(choices=[('KG', 'Kilogram'), ('UNIT', 'Unit'), ('PKT', 'Packets')], default='UNIT', max_length=255)),
            ],
        ),
    ]
