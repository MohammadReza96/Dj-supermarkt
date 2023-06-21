# Generated by Django 4.1.4 on 2023-05-12 17:35

from django.db import migrations, models
import modules.file_upload_module


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="auhtor_is_active",
            field=models.BooleanField(default=False, verbose_name="وضعیت"),
        ),
        migrations.AlterField(
            model_name="author",
            name="author_email",
            field=models.EmailField(max_length=255, verbose_name="ایمیل"),
        ),
        migrations.AlterField(
            model_name="author",
            name="author_family",
            field=models.CharField(max_length=50, verbose_name="نام خانوادگی"),
        ),
        migrations.AlterField(
            model_name="author",
            name="author_name",
            field=models.CharField(max_length=50, verbose_name="نام"),
        ),
        migrations.AlterField(
            model_name="author",
            name="author_phone",
            field=models.CharField(
                blank=True, max_length=11, null=True, verbose_name="شماره موبایل"
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="author_slug",
            field=models.SlugField(verbose_name="شناسه"),
        ),
        migrations.AlterField(
            model_name="blog",
            name="blog_main_image",
            field=models.ImageField(
                upload_to=modules.file_upload_module.FileUploader.upload_to,
                verbose_name="عکس کاور مقاله",
            ),
        ),
        migrations.AlterField(
            model_name="bloggallary",
            name="blog_image",
            field=models.ImageField(
                upload_to=modules.file_upload_module.FileUploader.upload_to,
                verbose_name="عکس مقاله",
            ),
        ),
        migrations.AlterField(
            model_name="bloggroup",
            name="group_title",
            field=models.CharField(max_length=20, verbose_name="عنوان"),
        ),
    ]
