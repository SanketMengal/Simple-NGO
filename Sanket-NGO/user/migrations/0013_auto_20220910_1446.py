# Generated by Django 3.2.4 on 2022-09-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_donateus_avalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donateus',
            name='avalue',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='donateus',
            name='ppic',
            field=models.ImageField(null=True, upload_to='static/profile/'),
        ),
    ]