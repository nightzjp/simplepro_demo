# Generated by Django 3.1 on 2020-08-26 02:39

from django.db import migrations, models
import django.db.models.deletion
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0017_studentclasses_studentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentOneToOneModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f', models.CharField(max_length=32, verbose_name='一对一')),
            ],
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='classes',
            field=simplepro.components.fields.ForeignKey(blank=True, help_text='一对多', null=True, on_delete=django.db.models.deletion.SET_NULL, to='components.studentclasses', verbose_name='班级'),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='one_to_one',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='components.studentonetoonemodel', verbose_name='一对一字段'),
        ),
    ]