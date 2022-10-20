# Generated by Django 4.1.1 on 2022-10-12 09:14

from django.db import migrations, models
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0046_inputnumbermodel_f2_inputnumbermodel_f3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CellActionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', simplepro.components.fields.CharField(max_length=32, verbose_name='名字')),
                ('desc', simplepro.components.fields.CharField(blank=True, max_length=32, null=True, verbose_name='描述')),
                ('status', models.BooleanField(default=False, verbose_name='状态')),
            ],
            options={
                'verbose_name': '单元格Action',
                'verbose_name_plural': '单元格Action',
            },
        ),
        migrations.CreateModel(
            name='TreeComboboxModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '树形下拉框',
                'verbose_name_plural': '树形下拉框',
            },
        ),
        migrations.AlterField(
            model_name='inputnumbermodel',
            name='f2',
            field=simplepro.components.fields.InputNumberField(default=1, help_text='继承自IntegerField'),
        ),
        migrations.AlterField(
            model_name='inputnumbermodel',
            name='f3',
            field=simplepro.components.fields.InputNumberField(default=1),
        ),
        migrations.AlterField(
            model_name='inputnumbermodel',
            name='f4',
            field=simplepro.components.fields.InputNumberField(default=1),
        ),
        migrations.AlterField(
            model_name='inputnumbermodel',
            name='f5',
            field=simplepro.components.fields.InputNumberField(default=1, verbose_name='计数器2'),
        ),
        migrations.AlterField(
            model_name='inputnumbermodel',
            name='f6',
            field=simplepro.components.fields.InputNumberField(default=1),
        ),
    ]
