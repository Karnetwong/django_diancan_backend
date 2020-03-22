from django.urls import path,include
from account.views import LoginView,PictureView,AddPicView,UpdatePicView,\
    FoodTypeView,UpdateTypeView,AddTypeView,ProductInfoView,\
    AddProductView,UpdateproductView,OrdercreateView,OrderlistView,OrderlistView1,OrderDetailView,\
    OrderCompleteView,OrderCancelView,CommentListView,CommentView,UserCommentListView,FoodIncomeFormView,UserView,GetUserInfoView,\
    OrderDeleView,OrderListSerch

urlpatterns = [
    path('login/',LoginView.as_view()),
    path('piclist/',PictureView.as_view()),
    path('addpic/',AddPicView.as_view()),
    path('updatepic/',UpdatePicView.as_view()),
    path('foodtype/',FoodTypeView.as_view()),
    path('updatetype/',UpdateTypeView.as_view()),
    path('addtype/',AddTypeView.as_view()),
    path('productlist/',ProductInfoView.as_view()),
    path('addproduct/',AddProductView.as_view()),
    path('updateproduct/',UpdateproductView.as_view()),
    path('orderlist/',OrderlistView.as_view()),
    path('orderlist1/',OrderlistView1.as_view()),
    path('orderlistserch/',OrderListSerch.as_view()),
    path('ordercreate/',OrdercreateView.as_view()),
    path('orderdetail/',OrderDetailView.as_view()),
    path('orderdele/',OrderDeleView.as_view()),
    path('ordercomplete/',OrderCompleteView.as_view()),
    path('ordercancel/',OrderCancelView.as_view()),
    path('comment/',CommentView.as_view()),
    path('commentlist/',CommentListView.as_view()),
    path('usercommentlist/',UserCommentListView.as_view()),
    path('foodincomeform/',FoodIncomeFormView.as_view()),
    path('user/',UserView.as_view()),
    path('getUserInfo/',GetUserInfoView.as_view()),
]