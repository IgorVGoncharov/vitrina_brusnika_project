# Generated by Django 5.1.4 on 2025-04-07 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_category_chapter_alter_category_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categories',
        ),
        migrations.RenameModel(
            old_name='Chapter',
            new_name='Chapters',
        ),
    ]
