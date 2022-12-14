# Generated by Django 4.1.3 on 2023-01-09 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                ("blogId", models.AutoField(primary_key=True, serialize=False)),
                ("blogname", models.CharField(max_length=200)),
                ("blogimg", models.FileField(upload_to="static/")),
                ("blogdesc", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=254)),
                ("number", models.CharField(blank=True, max_length=200)),
                ("question", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="SocialLinks",
            fields=[
                ("socialId", models.AutoField(primary_key=True, serialize=False)),
                ("socialmedianame", models.CharField(max_length=200)),
                ("link", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="WebsiteUser",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("fullname", models.CharField(max_length=50)),
                ("gender", models.CharField(max_length=50)),
                ("date", models.CharField(max_length=50)),
                ("month", models.CharField(max_length=50)),
                ("year", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("hour", models.CharField(max_length=50)),
                ("minute", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
            ],
        ),
    ]
