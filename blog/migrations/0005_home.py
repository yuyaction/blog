# Generated by Django 3.0.4 on 2020-03-16 20:27

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200317_0509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', markdownx.models.MarkdownxField(help_text='To Write with Markdown format', verbose_name='Contents')),
            ],
        ),
    ]
