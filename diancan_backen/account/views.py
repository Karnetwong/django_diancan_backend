from django.shortcuts import render
import hashlib
import json
import pymysql
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from account.models import SellerInfo,Picture,ProductCategory,ProductInfo,OrderMaster,OrderDetail,Comment,ProCategory,User
from account.serializers.picture_serial import PictureSerial
from account.serializers.foodtype_serial import Foodtypeserial
from account.serializers.productlist_serial import Productlistserial
from account.serializers.orderlistserial import OrderlistSerial
from account.serializers.orderdetailserial import OderDetailSerial
from account.serializers.comment_serial import CommentSerial
from account.serializers.user_serial import UserSerial
from account.serializers.productcategory_serial import ProductCategorySerial
# Create your views here.

class LoginView(APIView):
    def post(self,request,*args,**kwargs):
        username = request.data['username']
        password = request.data['password']
        # md5_password = hashlib.md5()
        # md5_password.update(password.encode())
        # password = md5_password.hexdigest()
        print(username,password)
        user = SellerInfo.objects.filter(username=username,password=password)
        if user !=None:
            ret = {
                "username": username,
                "user_id":user[0].seller_id,
                "code": 200,
                "msg": "登录成功",
            }
            return JsonResponse(ret)

class PictureView(APIView):
    def get(self,request,*args,**kwargs):
        picture_list = Picture.objects.filter().all()
        picture = PictureSerial(instance=picture_list,many=True)
        picture_list = json.dumps(picture.data,ensure_ascii=False)
        print(picture_list)
        return HttpResponse(picture_list)

import  datetime
class AddPicView(APIView):
    def post(self,request,*args,**kwargs):
        pic_url = request.data['pic_url']
        pic_message = request.data['description']
        create_time = datetime.datetime.now()
        update_time = datetime.datetime.now()
        picture = Picture()
        picture.pic_url = pic_url
        picture.pic_message = pic_message
        picture.create_time = create_time
        picture.update_time = update_time
        picture.save()
        print(11111)
        msg = {'code':'200','desc':'添加成功'}
        return JsonResponse(msg)

class UpdatePicView(APIView):
    def post(self,request,*args,**kwargs):
        pic_id = request.data['id']
        pic_url = request.data['pic_url']
        pic_message = request.data['description']
        update_time = datetime.datetime.now()
        picture = Picture.objects.filter(pic_id=pic_id).first()
        picture.pic_url = pic_url
        picture.pic_message = pic_message
        picture.update_time = update_time
        picture.save()
        print(11111)
        msg = {'code':'200','desc':'修改成功'}
        return JsonResponse(msg)

# class FoodTypeView(generics.ListAPIView):
#     queryset = ProductCategory.objects.all()
#     serializer_class = Foodtypeserial

from rest_framework.response import Response



class FoodTypeView(APIView):
    def get(self,request,*args,**kwargs):
        foodtype = ProCategory.objects.filter(category_type=1)
        foodtype_serial = Foodtypeserial(instance=foodtype,many=True)
        return Response(foodtype_serial.data)

# class FoodTypeView(APIView):
#     def get(self,request,*args,**kwargs):
#         foodtype = ProductCategory.objects.filter().all()
#         foodtype_serial = ProductCategorySerial(instance=foodtype,many=True)
#         return Response(foodtype_serial.data)


class AddTypeView(APIView):
    def post(self, request, *args, **kwargs):
        name = request.data['name']        # desc = request.data['desc']
        type = request.data['type']
        print(name,type)
        create_time = datetime.datetime.now()
        update_time = datetime.datetime.now()
        # if() 判断该type类型是否存在
        category = ProCategory.objects.create(name=name,category_type=type,create_time=create_time,update_time=update_time)
        print(category)
        print(11111)
        msg = {'code': '200', 'desc': '添加成功'}
        return JsonResponse(msg)



class UpdateTypeView(APIView):
    def post(self,request,*args,**kwargs):

        msg = {'code':'200','desc':'修改成功'}
        return  JsonResponse(msg)

class ProductInfoView(APIView):
    def post(self,request,*args,**kwargs):
        productlist = ProCategory.objects.filter(category_type=2).all()
        productlist = Productlistserial(instance=productlist, many=True)
        productlist = json.dumps(productlist.data, ensure_ascii=False)
        print(productlist)
        return HttpResponse(productlist)

class AddProductView(APIView):
    def post(self,request,*args,**kwargs):
        name = request.data['product_name']
        desc = request.data['product_description']
        parent_category_id = request.data['parent_category_id']
        product_price = request.data['product_price']
        product_stock = request.data['product_stock']
        product_icon = request.data['product_icon']
        category_type = 2
        create_time = datetime.datetime.now()
        update_time = datetime.datetime.now()
        print(category_type)
        product = ProCategory.objects.create(category_type=category_type,name=name,parent_category_id =parent_category_id,
                                             product_price = product_price,
                                             product_stock = product_stock,
                                             desc = desc,
                                             product_icon = product_icon,
                                             create_time = create_time,
                                             update_time = update_time)
        msg = {'code': '200', 'desc': '添加成功'}
        return JsonResponse(msg)
# class AddProductView(APIView):
#     def post(self,request,*args,**kwargs):
#         product_name = request.data['product_name']
#         product_description = request.data['product_description']
#         product_price = request.data['product_price']
#         product_stock = request.data['product_stock']
#         product_icon = request.data['product_icon']
#         category_type = request.data['category_type']
#         create_time = datetime.datetime.now()
#         update_time = datetime.datetime.now()
#         category = ProductCategory.objects.filter(category_id = category_type).first()
#         print(category.category_id)
#         product = ProductInfo.objects.create(product_name=product_name,
#                                              product_category_id =category.category_id,
#                                              product_price = product_price,
#                                              product_stock = product_stock,
#                                              product_description = product_description,
#                                              product_icon = product_icon,
#                                              category_type = category_type,
#                                              create_time = create_time,
#                                              update_time = update_time)
#         msg = {'code': '200', 'desc': '添加成功'}
#         return JsonResponse(msg)

class UpdateproductView(APIView):
    def post(self,request,*args,**kwargs):
        id = request.data['id']
        product_name = request.data['product_name']
        product_price = request.data['product_price']
        product_stock = request.data['product_stock']
        product_description = request.data['product_description']
        product_icon = request.data['product_icon']
        category_type = 2
        parent_category_id = request.data['parent_category_id']
        update_time = datetime.datetime.now()
        print(product_name)
        product = ProCategory.objects.filter(id=id).first()
        product.name = product_name
        product.product_price = product_price
        product.product_stock = product_stock
        product.desc = product_description
        product.product_icon = product_icon
        product.category_type = category_type
        product.parent_category_id = parent_category_id
        product.update_time = update_time
        product.save()
        msg = {'code': '200', 'desc': '添加成功'}
        return JsonResponse(msg)

# class OrderlistView1(APIView):
#     # 后端页面的list
#     def post(self,request,*args,**kwargs):
#         orderlist = OrderMaster.objects.filter().all()
#         orderlist = OrderlistSerial(instance=orderlist,many=True)
#         return Response(orderlist.data)

class OrderlistView1(generics.ListAPIView):
    queryset= OrderMaster.objects.filter().all()
    # print(queryset,11111)
    serializer_class = OrderlistSerial

# 后端订单查询：
class OrderListSerch(APIView):
    def post(self,request,*args,**kwargs):
        order_id = request.data['order_id']
        order_status = request.data['order_status']
        if order_id == '' :
            orderlistserch = OrderMaster.objects.filter(order_status=order_status).all()
            orderlistserch = OrderlistSerial(instance=orderlistserch,many=True)
            return HttpResponse(json.dumps(orderlistserch.data,ensure_ascii=False))
        orderlistserch = OrderMaster.objects.filter(order_id=order_id,order_status=order_status).all()
        orderlistserch = OrderlistSerial(instance=orderlistserch, many=True)
        return HttpResponse(json.dumps(orderlistserch.data, ensure_ascii=False))


class OrderDetailView(APIView):
    def post(self,request,*args,**kwargs):
        order_id = request.data['order_id']
        orderdetail = OrderDetail.objects.filter(order_id=order_id).all()
        orderdetail = OderDetailSerial(instance=orderdetail,many=True)
        orderdetail = json.dumps(orderdetail.data, ensure_ascii=False)
        print(type(orderdetail))
        return HttpResponse(orderdetail)

class OrderlistView(APIView):
    # 小程序的list
    def post(self,request,*args,**kwargs):
        order_status = request.data['order_status']
        print(order_status)
        orderlist = OrderMaster.objects.filter(order_status=order_status).all()
        # 修改订单状态
        for item in orderlist:
            item.orderStatusStr = item.get_order_status_display()
            item.save()
        orderlist = OrderlistSerial(instance=orderlist,many=True)
        return Response(orderlist.data)

from account.consumers import push
import time
class OrdercreateView(APIView):
    def post(self,request,*args,**kwargs):
        openid = request.data['openid']
        name = request.data['name']
        phone = request.data['phone']
        address = request.data['address']
        items = request.data['items']
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        jsonitems  = json.loads(items)
        print(jsonitems)
        order_amount = 0
        for foods in jsonitems:
            # 库存
            food = ProCategory.objects.filter(category_type=2,id = foods['productId']).first()
            print(food,2222222)
            food.product_stock = int(food.product_stock)-int(foods['productQuantity'])
            food.save()
            food = Productlistserial(instance=food,many=False)
            print(food,333333)
            food  = json.dumps(food.data, ensure_ascii=False)
            food  = json.loads(food)
            print(food,111111)
            # 总价
            order_amount += float(food['product_price'])*int(foods['productQuantity'])

        orderlist = OrderMaster.objects.create(buyer_openid=openid,
                                               buyer_name=name,
                                               buyer_phone=phone,
                                               buyer_address=address,
                                               order_amount = order_amount,
                                               create_time=create_time,
                                               update_time = update_time,
                                               )
        # 添加orderStatusStr
        orderlist.orderStatusStr = orderlist.get_order_status_display()
        orderlist.save()
        for foods in jsonitems:
            food = ProCategory.objects.filter(category_type=2,id = foods['productId']).first()
            food = Productlistserial(instance=food,many=False)
            food  = json.dumps(food.data, ensure_ascii=False)
            food  = json.loads(food)
            print(food,1111223)
            orderDetail = OrderDetail.objects.create(product_id = food['id'],
                                                     product_name=food['name'],
                                                     product_price=food['product_price'],
                                                     product_quantity=foods['productQuantity'],
                                                     product_icon=food['product_icon'],
                                                     create_time =create_time,
                                                     update_time = update_time,
                                                     orderMaster_id=orderlist.order_id,
                                                     order_id = orderlist.order_id
                                                     )
        msg = {'code': '200', 'desc': '添加成功'}
        # 发送websocket消息
        push()
        return JsonResponse(msg)

class OrderDeleView(APIView):
    def post(self,request,*args,**kwargs):
        order_id = request.data['id']
        OrderMaster.objects.filter(order_id = order_id).delete()
        ret ={"code":"200","msg":"删除成功"}
        return JsonResponse(ret)

class OrderCompleteView(APIView):
    def post(self,request,*args,**kwargs):
        order_status = request.data['order_status']
        order_id = request.data['order_id']
        print(order_status,order_id)
        ordermaster = OrderMaster.objects.filter(order_id=order_id).first()
        ordermaster.order_status = order_status
        ordermaster.orderStatusStr = ordermaster.get_order_status_display()
        ordermaster.save()
        msg = {'code': '200', 'desc': '完成订单'}
        return JsonResponse(msg)

class OrderCancelView(APIView):
    def post(self,request,*args,**kwargs):
        order_status = request.data['order_status']
        order_id = request.data['order_id']
        ordermaster = OrderMaster.objects.filter(order_id=order_id).first()
        ordermaster.order_status = order_status
        ordermaster.orderStatusStr = ordermaster.get_order_status_display()
        ordermaster.save()
        msg = {'code': '200', 'desc': '取消订单'}
        return JsonResponse(msg)

class CommentView(APIView):
    def post(self,request,*args,**kwargs):
        orderId = request.data['orderId']
        openid = request.data['openid']
        name = request.data['name']
        avatarUrl = request.data['avatarUrl']
        content = request.data['content']
        createtime = datetime.datetime.now()
        comment = Comment.objects.create(
            openid = openid,
            name =name,
            create_time= createtime,
            avatar_url = avatarUrl,
            content = content
        )
        order = OrderMaster.objects.filter(order_id = orderId).first()
        order.order_status = 4
        order.save()
        return HttpResponse(1)

class CommentListView(APIView):
    def post(self,request,*args,**kwargs):
        commentlist = Comment.objects.filter().all()
        commentlist = CommentSerial(instance=commentlist,many=True)
        commentlist = json.dumps(commentlist.data,ensure_ascii=False)

        return HttpResponse(commentlist)

class UserCommentListView(APIView):
    def post(self,request,*args,**kwargs):
        openid = request.data['openid']
        usercomment = Comment.objects.filter(openid=openid).all()
        usercommentlist = CommentSerial(instance=usercomment, many=True)
        usercommentlist = json.dumps(usercommentlist.data,ensure_ascii=False)
        return HttpResponse(usercommentlist)

import copy
class FoodIncomeFormView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            db = pymysql.connect(
                host="127.0.0.1",
                port=3306,
                user="root",
                password="zx8302335",
                charset="utf8",
                db="mysell"
            )
            cursor = db.cursor()
            sql = """
                select extract(year_month from create_time),sum(order_amount) 
                from account_ordermaster where account_ordermaster.order_status != '2' 
                group by extract(year_month from create_time)
            """
            cursor.execute(sql)
            income = cursor.fetchall()
            db.close()
            print(income,1)
            income_dict = {'create_time':[],'total':[]}
            income = list(income)
            # income.reverse()
            for obj in income:
                # income_list = copy.deepcopy(dict(zip(income_list, list(obj))))
                income_dict['create_time'].append(obj[0])
                income_dict['total'].append(float(obj[1]))
            list1 = json.dumps(income_dict)
            return HttpResponse(list1)
        except Exception as e:
            # 回滚
            msg = {'error': '404'}
            return HttpResponse(json.dumps(msg))


class UserView(APIView):
    def post(self,request,*args,**kwargs):
        username = request.data['username']
        phone = request.data['phone']
        openid = request.data['openid']
        zhuohao = request.data['zhuohao']
        renshu = request.data['renshu']
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        user = User.objects.create(username=username,phone=phone,openid=openid,zhuohao=zhuohao,
                                   renshu=renshu,create_time=create_time,update_time=update_time)
        return HttpResponse(1)

class GetUserInfoView(APIView):
    def post(self,request,*args,**kwargs):
        openid = request.data['openid']
        user = User.objects.filter(openid=openid)
        user = UserSerial(instance=user,many=True)
        user = json.dumps(user.data,ensure_ascii=False)
        return HttpResponse(user)