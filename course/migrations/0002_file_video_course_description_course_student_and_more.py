# Generated by Django 4.2.4 on 2023-09-02 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_customuser_status"),
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("file", models.FileField(upload_to="course_files/")),
            ],
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("video", models.FileField(upload_to="course_videos/")),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="description",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="course",
            name="student",
            field=models.ManyToManyField(to="user.etudiant"),
        ),
        migrations.AddField(
            model_name="course",
            name="thumbnail",
            field=models.ImageField(default="", upload_to="course_thumbnails/"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="course",
            name="title",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="course",
            name="file",
            field=models.ManyToManyField(to="course.file"),
        ),
        migrations.AddField(
            model_name="course",
            name="video",
            field=models.ManyToManyField(to="course.video"),
        ),
    ]
