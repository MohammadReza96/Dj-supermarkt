# Generated by Django 4.1.4 on 2023-04-07 14:45

from django.db import migrations, models
import modules.file_upload_module


class Migration(migrations.Migration):

    dependencies = [
        (
            "products",
            "0005_alter_brand_brand_image_alter_product_product_image_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="brand_image",
            field=models.ImageField(
                upload_to=modules.file_upload_module.FileUploader.upload_to,
                verbose_name="تصویر برند",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_image",
            field=models.ImageField(
                upload_to=modules.file_upload_module.FileUploader.upload_to,
                verbose_name="تصویر محصول",
            ),
        ),
        migrations.AlterField(
            model_name="productgallary",
            name="product_gallary_image",
            field=models.ImageField(
                upload_to=modules.file_upload_module.FileUploader.upload_to,
                verbose_name="تصویر محصول",
            ),
        ),
        migrations.AlterField(
            model_name="productgroup",
            name="group_image",
            field=models.ImageField(
                upload_to=modules.file_upload_module.FileUploader.upload_to,
                verbose_name="تصویر گروه کالا",
            ),
        ),
    ]
