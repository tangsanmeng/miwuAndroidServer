from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 登录验证
    path('verify/', views.test_connect),
    # 注册
    path('register/', views.register),
    # 修改用户名
    path('changeName/', views.change_name),
    # 商品提交
    path('commoditySubmit/', views.commodity_submit),
    # 查看我发布的商品
    path('Mycommodity/', views.my_commodity_list),
    # 查看所有商品
    path('CommodityList/', views.commodity_list),
    # 商品细节
    path('CommodityDetail/', views.commodity_detail),
    # 用户购买商品
    path('CommodityBuyed/', views.CommodityBuyed),
    # 用户查看所购买的商品
    path('CommodityBuyList/', views.commodity_buy_list),
    # 用户发表商品评论
    path('CommodityCommentSubmit/', views.commodity_comment_submit),
    # 商品的删除
    path('CommodityDelete/', views.commodity_delete),

    # 测试
    path('demo/', views.demo),
]