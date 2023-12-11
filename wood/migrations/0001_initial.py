# Generated by Django 5.0 on 2023-12-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('date_task_created', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(null=True)),
                ('status', models.BooleanField(null=True)),
                ('tags', models.ManyToManyField(related_name='tag', to='wood.tags')),
            ],
        ),
    ]
