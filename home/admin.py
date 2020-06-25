from django.contrib import admin

# Register your models here.
from home.models import *


class InfoCategory(admin.ModelAdmin):
    list_display = ('category_name', 'category_parent_id', 'category_id', 'category_status')


class InfoBrand(admin.ModelAdmin):
    list_display = ('brand_name', 'brand_id', 'brand_status')


class InfoProduct(admin.ModelAdmin):
    list_display = ('product_id', 'category_id', 'brand_id', 'product_name', 'product_price', 'product_quantity', 'product_status')


class InfoBlock(admin.ModelAdmin):
    list_display = ('blog_id', 'blog_title', 'block_status')


class InfoBlockDetail(admin.ModelAdmin):
    list_display = ('block_id', 'block_detail_id', 'block_detail_title', 'block_detail_status')


admin.site.register(Category, InfoCategory)
admin.site.register(BlockDetail, InfoBlockDetail)
admin.site.register(Blog, InfoBlock)
admin.site.register(Brand, InfoBrand)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Product, InfoProduct)
admin.site.register(ProductImages)
admin.site.register(Promotion)
