# Generated by Django 4.2.4 on 2023-08-26 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='videos',
            field=models.ManyToManyField(related_name='courses', to='courses.video'),
        ),
    ]
