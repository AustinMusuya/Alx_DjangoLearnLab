# Generated by Django 5.1.3 on 2024-12-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_created_at_alter_post_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ManyToManyField(to='blog.post', verbose_name='list of post_tags')),
            ],
        ),
    ]