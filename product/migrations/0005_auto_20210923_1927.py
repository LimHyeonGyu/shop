# Generated by Django 3.2.6 on 2021-09-23 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_pro_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '상품관리'},
        ),
        migrations.AlterField(
            model_name='product',
            name='pro_status',
            field=models.CharField(choices=[('f', 'Fruit'), ('p', 'Phone'), ('c', 'Computer')], max_length=1, null=True, verbose_name='카테고리'),
        ),
    ]