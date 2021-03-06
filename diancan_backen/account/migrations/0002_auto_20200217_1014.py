# Generated by Django 2.1.3 on 2020-02-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermaster',
            name='orderStatusStr',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='order_status',
            field=models.IntegerField(choices=[(1, '已支付'), (4, '已完成'), (3, '待评价'), (2, '已取消')], default=1),
        ),
    ]
