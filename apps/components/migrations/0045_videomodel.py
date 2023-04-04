# Generated by Django 4.0.2 on 2022-06-13 04:26

from django.db import migrations, models
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0044_alter_layer_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', simplepro.components.fields.CharField(blank=True, max_length=64, null=True, verbose_name='名称')),
                ('video', simplepro.components.fields.VideoField(blank=True, help_text='视频播放组件', max_length=128, null=True, verbose_name='视频播放')),
            ],
            options={
                'verbose_name': '视频播放组件',
                'verbose_name_plural': '视频播放组件',
            },
        ),
    ]