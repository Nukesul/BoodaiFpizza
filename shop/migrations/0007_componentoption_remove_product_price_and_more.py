# Generated by Django 4.2 on 2025-03-28 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_compatible_with_product_component_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название комплектующего (например, Intel i7)', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, help_text='Дополнительная стоимость', max_digits=10)),
                ('volume', models.CharField(blank=True, help_text='Объем/характеристика (например, 16GB)', max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='base_price',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Базовая цена без учета комплектующих', max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='model_3d',
            field=models.FileField(blank=True, help_text='3D модель в формате .glb', null=True, upload_to='3d_models/'),
        ),
        migrations.AddField(
            model_name='product',
            name='components',
            field=models.ManyToManyField(blank=True, help_text='Доступные комплектующие', to='shop.componentoption'),
        ),
    ]
