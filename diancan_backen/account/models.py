# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    openid = models.CharField(max_length=64)
    content = models.TextField()
    avatar_url = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()

class OrderMaster(models.Model):
    order_status = {
        (1, "已支付"),
        (2, "已取消"),
        (3, "待评价"),
        (4, "已完成"),
    }
    order_id = models.AutoField(primary_key=True, max_length=32)
    buyer_name = models.CharField(max_length=32)
    buyer_phone = models.CharField(max_length=32)
    buyer_address = models.CharField(max_length=128)
    buyer_openid = models.CharField(max_length=64)
    order_amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_status = models.IntegerField(choices=order_status,default=1)
    orderStatusStr = models.CharField(max_length=32,null=True)
    pay_status = models.IntegerField(default=0)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    # orderDetail = models.ForeignKey(OrderDetail,related_name="sub_cat",on_delete=models.CASCADE,default=1)

class OrderDetail(models.Model):
    detail_id = models.AutoField(primary_key=True, max_length=32)
    order_id = models.CharField(max_length=32)
    product_id = models.CharField(max_length=32)
    product_name = models.CharField(max_length=64)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = models.IntegerField()
    product_icon = models.CharField(max_length=512, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    orderMaster = models.ForeignKey(OrderMaster,related_name='master_detail',to_field='order_id',on_delete=models.CASCADE,default='')

#
#
class Picture(models.Model):
    pic_id = models.AutoField(primary_key=True)
    pic_url = models.CharField(max_length=255)
    pic_message = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()



class ProCategory(models.Model):
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
    )
    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    product_icon = models.CharField(max_length=512, blank=True, null=True)
    product_price = models.DecimalField(max_digits=8, decimal_places=2,null=True)
    product_stock = models.IntegerField(null=True)
    product_status = models.IntegerField(blank=True, null=True, default=0)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

class ProductCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=64)
    category_type = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

class ProductInfo(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=64)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_stock = models.IntegerField()
    product_description = models.CharField(max_length=64, blank=True, null=True)
    product_icon = models.CharField(max_length=512, blank=True, null=True)
    product_status = models.IntegerField(blank=True, null=True,default=0)
    category_type = models.CharField(max_length=8)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    product_category = models.ForeignKey(ProductCategory, related_name='sub_cat', to_field='category_id',
                                         on_delete=models.CASCADE, default='')



class SellerInfo(models.Model):
    seller_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()


class User(models.Model):
    username = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    openid = models.CharField(max_length=64)
    zhuohao = models.CharField(max_length=64, blank=True, null=True)
    renshu = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'user'
