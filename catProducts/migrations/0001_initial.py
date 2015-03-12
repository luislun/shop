# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catBrands', '0001_initial'),
        ('catProductCategories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=20, decimal_places=6)),
                ('brand', models.ForeignKey(to='catBrands.CatBrand')),
                ('category_level_1', models.ForeignKey(related_name='category_level_1', to='catProductCategories.CatProductCategory')),
                ('category_level_2', models.ForeignKey(related_name='category_level_2', blank=True, to='catProductCategories.CatProductCategory', null=True)),
                ('category_level_3', models.ForeignKey(related_name='category_level_3', blank=True, to='catProductCategories.CatProductCategory', null=True)),
                ('category_level_4', models.ForeignKey(related_name='category_level_4', blank=True, to='catProductCategories.CatProductCategory', null=True)),
                ('category_level_5', models.ForeignKey(related_name='category_level_5', blank=True, to='catProductCategories.CatProductCategory', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
