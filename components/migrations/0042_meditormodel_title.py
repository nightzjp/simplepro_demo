# Generated by Django 3.2 on 2022-02-15 14:55

from django.db import migrations
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0041_auto_20220215_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='meditormodel',
            name='title',
            field=simplepro.components.fields.CharField(blank=True, max_length=128, null=True, verbose_name='标题'),
        ),
    ]