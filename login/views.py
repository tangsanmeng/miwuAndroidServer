import json

import leancloud
from django.http import HttpResponse
from PIL import Image


def test_connect(request):

    print("登录校验API被调用")
    if request.method == 'POST':
        leancloud.init("ILpxKphAjAghfoPeZkNVtN0w-gzGzoHsz", "jI1kxeh2mhYrSfzZHapy5Y3w")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("接收到的username: " + username + "  password: " + password)
        try:
            user = leancloud.User()
            user.login(username=username, password=password)
        except leancloud.LeanCloudError as e:
            print(e)
            date_msg = {
                'msg': '错误，用户不存在或密码错误!',
                'code': "100"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')

        Todo = leancloud.Object.extend('_User')
        query = Todo.query
        query.equal_to('username', username)
        todo = query.first()
        date_msg = {
            'msg': '成功！',
            'yonghuming': todo.get('yonghuming'),
            'yonghuId': todo.get("objectId"),
            'code': "101"
        }
        return HttpResponse(json.dumps(date_msg), content_type='application/json')
    else:
        date_msg = {
            'msg': 'GET请求不受理',
            'code': "99"
        }
        return HttpResponse(json.dumps(date_msg), content_type='application/json')


def register(request):

    print("注册API被调用")
    if request.method == 'POST':
        leancloud.init("ILpxKphAjAghfoPeZkNVtN0w-gzGzoHsz", "jI1kxeh2mhYrSfzZHapy5Y3w")
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        print(username, password, phone)
        if username and password and phone:
            try:
                Todo = leancloud.Object.extend('_User')
                todo = Todo()
                todo.set("username", username)
                todo.set("yonghuming", username)
                todo.set("password", password)
                todo.set("mobilePhoneNumber", phone)
                todo.save()
            except leancloud.LeanCloudError as e:
                date_msg = {
                    'msg': e,
                    'code': "103"
                }
                return HttpResponse(json.dumps(date_msg), content_type='application/json')
            date_msg = {
                'msg': "注册成功!",
                'code': "102"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
        else:
            date_msg = {
                'msg': '手机格式出错或服务器连接失败!',
                'code': "103"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
    else:
        date_msg = {
            'msg': 'GET请求不受理',
            'code': "99"
        }
        return HttpResponse(json.dumps(date_msg), content_type='application/json')


def change_name(request):
    print("用户名API被调用")
    if request.method == 'POST':
        leancloud.init("ILpxKphAjAghfoPeZkNVtN0w-gzGzoHsz", master_key="WjU2KJJs1P5wlpoxenewLmgy")
        new_name = request.POST.get('yonghuming')
        username = request.POST.get('username')
        print(new_name)
        print("username", username)
        if new_name:
            try:
                Todo = leancloud.User
                query = Todo.query
                query.equal_to('username', username)
                todo = query.first()
                objectId = todo.id

                Todo = leancloud.Object.extend('_User')
                todo = Todo.create_without_data(objectId)
                todo.set('yonghuming', new_name)
                todo.save()
            except leancloud.LeanCloudError as e:
                print(e)
                date_msg = {
                    'msg': e,
                    'code': "104"
                }
                return HttpResponse(json.dumps(date_msg), content_type='application/json')
            date_msg = {
                'msg': '修改成功！',
                'yonghuming': new_name,
                'objectId': objectId,
                'code': "105"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
        else:
            date_msg = {
                'msg': '接收值为空！',
                'code': "106"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
    else:
        date_msg = {
            'msg': 'GET请求不受理',
            'code': "99"
        }
        return HttpResponse(json.dumps(date_msg), content_type='application/json')


def commodity_submit(request):

    if request.method == 'POST':
        leancloud.init("ILpxKphAjAghfoPeZkNVtN0w-gzGzoHsz", master_key="WjU2KJJs1P5wlpoxenewLmgy")
        print("asdasd")
        info = request.POST.get("info")
        file = request.FILES.get("file")
        price = request.POST.get("price")
        maijia_address = request.POST.get("maijia_address")
        username = request.POST.get("username")  # 用于获取用户objectId

        if info and file and price and maijia_address and username:
            img = Image.open(file)
            img.save('d:/djangoProject/AndriodSever/picture/demo.jpg')
            f = open('d:/djangoProject/AndriodSever/picture/demo.jpg', 'rb')
            file = leancloud.File('demo.jpg', f)
            try:
                Todo = leancloud.User
                query = Todo.query
                query.equal_to('username', username)
                todo = query.first()
                objectId = todo.id

                print("objectId: ", objectId)

                Todo = leancloud.Object.extend('commodityinfo')
                todo = Todo()
                todo.set('commodityIntroduction', info)
                todo.set('maijia_address', maijia_address)
                todo.set('commodityfrom', objectId)
                todo.set('price', price)
                todo.set('picture', file)
                todo.set('flag', "114514")

                print("commodityIntroduction: ", info)
                print("maijia_address: ", maijia_address)
                print("price: ", price)


                todo.save()
                date_msg = {
                    'msg': '上传成功!',
                    'code': "107"
                }
                return HttpResponse(json.dumps(date_msg), content_type='application/json')
            except leancloud.LeanCloudError as e:
                print(e)
                date_msg = {
                    'msg': e,
                    'code': "108"
                }
                return HttpResponse(json.dumps(date_msg), content_type='application/json')
        else:
            date_msg = {
                'msg': '接收值中含有空值!',
                'code': "109"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
    else:
        date_msg = {
            'msg': 'GET请求不受理',
            'code': "99"
        }
        return HttpResponse(json.dumps(date_msg), content_type='application/json')


def my_commodity_list(request):

    info = []
    price = []
    commodityfrom = []
    picture = []
    maijia_address = []
    createAt = []
    id = []

    if request.method == 'POST':
        leancloud.init("ILpxKphAjAghfoPeZkNVtN0w-gzGzoHsz", master_key="WjU2KJJs1P5wlpoxenewLmgy")
        username = request.POST.get("username")

        try:
            Todo = leancloud.User
            query = Todo.query
            query.equal_to('username', username)
            todo = query.first()
            objectId = todo.id

            commodity = leancloud.Object.extend('commodityinfo')

            query1 = commodity.query
            query1.equal_to('commodityfrom', objectId)

            query2 = commodity.query
            query2.equal_to('flag', "114514")

            query = leancloud.Query.and_(query1, query2)
            commodity_list = query.find()

            count = query.count()

            print(commodity_list)
            print(str(commodity_list))

            for temp in commodity_list:
                info.append(temp.get("commodityIntroduction"))
                price.append(temp.get("price"))
                picture.append(temp.get("picture").url)
                maijia_address.append(temp.get("maijia_address"))
                createAt.append(temp.created_at.strftime('%Y-%m-%d %H:%M'))
                id.append(temp.id)

                Todo = leancloud.Object.extend('_User')
                query = Todo.query
                query.equal_to('objectId', temp.get("commodityfrom"))
                todo = query.first()

                commodityfrom.append(todo.get("yonghuming"))

            # print("info: ", info)
            # print("price: ", price)
            # print("commoditufrom: ", commodityfrom)
            # print("picture: ", picture)
            # print("maijia_address: ", maijia_address)
            # print("createAt: ", createAt)
            # print("id: ", id)

            dict_list = []
            for i in range(count):
                print(i)
                dict_object = {"commodityIntroduction": info[i], "price": price[i], "maijia_address": maijia_address[i], "commodityfrom": commodityfrom[i], "createAt": createAt[i], "picture": picture[i], "id": id[i]}
                dict_list.append(dict_object)
            print(dict_list)

            date_msg = {
                'msg': "查询成功！",
                'code': "110",
                'list': dict_list
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
        except leancloud.LeanCloudError as e:
            print(e)
            date_msg = {
                'msg': e,
                'code': "111"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
    else:
        date_msg = {
            'msg': 'GET请求不受理',
            'code': "99"
        }
        return HttpResponse(json.dumps(date_msg), content_type='application/json')


def commodity_list(request):

    info = []
    price = []
    commodityfrom = []
    picture = []
    maijia_address = []
    createAt = []
    id = []

    if request.method == "POST":
        leancloud.init("ILpxKphAjAghfoPeZkNVtN0w-gzGzoHsz", master_key="WjU2KJJs1P5wlpoxenewLmgy")
        try:
            commodity = leancloud.Object.extend('commodityinfo')
            query = commodity.query
            # 以上两行等价于 query = leancloud.Query('Student')
            query.equal_to('flag', "114514")
            commodity_list = query.find()
            count = query.count()

            for temp in commodity_list:

                info.append(temp.get("commodityIntroduction"))
                price.append(temp.get("price"))
                picture.append(temp.get("picture").url)
                maijia_address.append(temp.get("maijia_address"))
                createAt.append(temp.created_at.strftime('%Y-%m-%d %H:%M'))
                id.append(temp.id)

                Todo = leancloud.Object.extend('_User')
                query = Todo.query
                query.equal_to('objectId', temp.get("commodityfrom"))
                todo = query.first()
                commodityfrom.append(todo.get("yonghuming"))

            dict_list = []
            for i in range(count):
                dict_object = {"commodityIntroduction": info[i], "price": price[i], "maijia_address": maijia_address[i],
                               "commodityfrom": commodityfrom[i], "createAt": createAt[i], "picture": picture[i],
                               "id": id[i]}
                dict_list.append(dict_object)
            print(dict_list)

            date_msg = {
                'msg': "查询成功！",
                'code': "112",
                'list': dict_list
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
        except leancloud.LeanCloudError as e:
            print(e)
            date_msg = {
                'msg': e,
                'code': "113"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')

    else:
        date_msg = {
            'msg': 'GET请求不受理',
            'code': "99"
        }
        return HttpResponse(json.dumps(date_msg), content_type='application/json')


def commodity_detail(request):

    # 用以存储评论/留言信息的列表
    comment_detail = []
    comment_at = []
    comment_from = []

    if request.method == "POST":
        leancloud.init("ILpxKphAjAghfoPeZkNVtN0w-gzGzoHsz", master_key="WjU2KJJs1P5wlpoxenewLmgy")
        objectId = request.POST.get("objectId")
        try:
            # 根据商品id拿到商品的具体信息
            Todo = leancloud.Object.extend('commodityinfo')
            query = Todo.query
            query.equal_to('objectId', objectId)
            todo = query.first()

            info = todo.get("commodityIntroduction")
            price = todo.get("price")
            maijia_address = todo.get("maijia_address")
            createAt = todo.created_at.strftime('%m-%d %H:%M')
            commodityfrom = todo.get("commodityfrom")
            picture = todo.get("picture").url

            # 根据从商品信息中拿到的用户id去User表中寻找用户的用户名
            Todo = leancloud.Object.extend('_User')
            query = Todo.query
            query.equal_to('objectId', commodityfrom)
            todo = query.first()
            commodityfrom = todo.get("yonghuming")

            # 再根据商品id寻找comment中对应的评论
            Todo = leancloud.Object.extend('comment')
            query = Todo.query
            query.equal_to('commentbelong', objectId)
            comment_list = query.find()
            count = query.count()

            for temp in comment_list:
                comment_detail.append(temp.get("commentdetail"))
                comment_at.append(temp.created_at.strftime('%Y-%m-%d %H:%M'))

                Todo = leancloud.Object.extend('_User')
                query = Todo.query
                query.equal_to('objectId', temp.get("commentfrom"))
                todo = query.first()
                comment_from.append(todo.get("yonghuming"))

            # 构建dict_list列表存储此商品的评论信息
            dict_list = []
            for i in range(count):
                dict_object = {"comment_from": comment_from[i], "comment_detail": comment_detail[i], "comment_at": comment_at[i]}
                dict_list.append(dict_object)

            date_msg = {
                'msg': '查询成功！',
                'code': "114",
                'info': info,
                'price': price,
                'maijia_address': maijia_address,
                'createAt': createAt,
                'commodityfrom': commodityfrom,
                'picture': picture,
                'list': dict_list
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
        except leancloud.LeanCloudError as e:
            print(e)
            date_msg = {
                'msg': e,
                'code': "115"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
    else:
        date_msg = {
            'msg': 'GET请求不受理',
            'code': "99"
        }
        return HttpResponse(json.dumps(date_msg), content_type='application/json')


def CommodityBuyed(request):
    if request.method == "POST":
        leancloud.init("ILpxKphAjAghfoPeZkNVtN0w-gzGzoHsz", master_key="WjU2KJJs1P5wlpoxenewLmgy")
        commodityID = request.POST.get("commodityId")
        objectId = request.POST.get("objectId")

        try:
            Todo = leancloud.Object.extend('commodityinfo')
            print("commodityID:::::", commodityID)
            todo = Todo.create_without_data(commodityID)
            todo.set("flag", objectId)
            todo.save()

            date_msg = {
                'msg': "购买成功！",
                'code': "116"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
        except leancloud.LeanCloudError as e:
            print(e)
            date_msg = {
                'msg': e,
                'code': "117"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
    else:
        date_msg = {
            'msg': 'GET请求不受理',
            'code': "99"
        }
        return HttpResponse(json.dumps(date_msg), content_type='application/json')


def commodity_buy_list(request):

    info = []
    price = []
    commodityfrom = []
    picture = []
    maijia_address = []
    createAt = []
    id = []

    if request.method == 'POST':
        leancloud.init("ILpxKphAjAghfoPeZkNVtN0w-gzGzoHsz", master_key="WjU2KJJs1P5wlpoxenewLmgy")
        username = request.POST.get("username")

        try:
            Todo = leancloud.User
            query = Todo.query
            query.equal_to('username', username)
            todo = query.first()
            objectId = todo.id

            commodity = leancloud.Object.extend('commodityinfo')
            query = commodity.query
            query.equal_to('flag', objectId)
            commodity_list = query.find()
            count = query.count()

            print(commodity_list)
            print(str(commodity_list))

            for temp in commodity_list:
                info.append(temp.get("commodityIntroduction"))
                price.append(temp.get("price"))
                picture.append(temp.get("picture").url)
                maijia_address.append(temp.get("maijia_address"))
                createAt.append(temp.created_at.strftime('%Y-%m-%d %H:%M'))
                id.append(temp.id)

                Todo = leancloud.Object.extend('_User')
                query = Todo.query
                query.equal_to('objectId', temp.get("commodityfrom"))
                todo = query.first()

                commodityfrom.append(todo.get("yonghuming"))

            # print("info: ", info)
            # print("price: ", price)
            # print("commoditufrom: ", commodityfrom)
            # print("picture: ", picture)
            # print("maijia_address: ", maijia_address)
            # print("createAt: ", createAt)
            # print("id: ", id)

            dict_list = []
            for i in range(count):
                print(i)
                dict_object = {"commodityIntroduction": info[i], "price": price[i], "maijia_address": maijia_address[i], "commodityfrom": commodityfrom[i], "createAt": createAt[i], "picture": picture[i], "id": id[i]}
                dict_list.append(dict_object)
            print(dict_list)

            date_msg = {
                'msg': "查询成功！",
                'code': "118",
                'list': dict_list
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
        except leancloud.LeanCloudError as e:
            print(e)
            date_msg = {
                'msg': e,
                'code': "119"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
    else:
        date_msg = {
            'msg': 'GET请求不受理',
            'code': "99"
        }
        return HttpResponse(json.dumps(date_msg), content_type='application/json')


def commodity_comment_submit(request):
    if request.method == 'POST':
        leancloud.init("ILpxKphAjAghfoPeZkNVtN0w-gzGzoHsz", master_key="WjU2KJJs1P5wlpoxenewLmgy")
        objectId = request.POST.get("objectId")
        commodityId = request.POST.get("commodityId")
        commentDetail = request.POST.get("commentDetail")
        try:
            # 声明 class
            Todo = leancloud.Object.extend('comment')
            # 构建对象
            todo = Todo()
            # 为属性赋值
            todo.set('commentbelong', commodityId)
            todo.set('commentdetail', commentDetail)
            todo.set('commentfrom', objectId)
            # 将对象保存到云端
            todo.save()

            date_msg = {
                'msg': "评论提交成功！",
                'code': "120"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')

        except leancloud.LeanCloudError as e:
            print(e)
            date_msg = {
                'msg': e,
                'code': "121"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
    else:
        date_msg = {
            'msg': 'GET请求不受理',
            'code': "99"
        }
        return HttpResponse(json.dumps(date_msg), content_type='application/json')


def commodity_delete(request):
    if request.method == 'POST':
        leancloud.init("ILpxKphAjAghfoPeZkNVtN0w-gzGzoHsz", master_key="WjU2KJJs1P5wlpoxenewLmgy")
        objectId = request.POST.get("objectId")
        try:
            Todo = leancloud.Object.extend('commodityinfo')
            todo = Todo.create_without_data(objectId)
            todo.destroy()

            date_msg = {
                'msg': "删除成功！",
                'code': "122"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
        except leancloud.LeanCloudError as e:
            print(e)
            date_msg = {
                'msg': e,
                'code': "123"
            }
            return HttpResponse(json.dumps(date_msg), content_type='application/json')
    else:
        date_msg = {
            'msg': 'GET请求不受理',
            'code': "99"
        }
        return HttpResponse(json.dumps(date_msg), content_type='application/json')


def demo(request):
    if request.method == 'GET':
        date_msg = {
            'msg': 'GET请求不受理',
            'code': "99"
        }
        return HttpResponse(json.dumps(date_msg), content_type='application/json')