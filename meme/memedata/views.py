from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
# from memedata.models import *
from memedata.models import *
from memedata.serializers import TestUserSerializer,TestStarSerializer
from rest_framework.views import APIView
import time
import pymongo
import json
import os
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.views.generic import View

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings


# Create your views here.


# 测试函数
def test(request):
    return render(request, "upload.html")

def index(request):

    testusers=TestUser.objects.all()
    return render(request, "index.html", {"testusers":testusers})

# 头像上传
def upload(request):
    if request.method == 'POST':
        user = User()
        # 把文件写入到服务器中
        name = request.POST.get('username')
        file_avatar = request.FILES.get('avatar')
        file_name = file_avatar.name
        file_path = os.path.join(settings.MEDIA_ROOT,'avatars/images',file_name)
        print(file_path)
        with open(file_path,'wb') as f:
           for chunk in file_avatar.chunks():
              f.write(chunk)
        # 把文件上传到数据库中
        user.avatar = os.path.join("avatars/images",file_name)
        return HttpResponse('ok')
    return render(request,'upload.html')




@login_required
def test_user(request):
    testusers = TestUser.objects.all()
    return render(request, "test_user.html", {"testusers": testusers})

@login_required
def test_star(request):
    teststars = TestStar.objects.all()
    return render(request, "test_star.html", {"teststars": teststars})

#退出
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/memedata/api/v1/login/')





# 注册
def register(request):
    return render(request, 'register.html')
# 注册处理
def regsiter_handler(request):
    request_params=request.POST
    user_name=request_params.get("username")
    user_pwd=request_params.get("pwd")
    user=User.objects.create_user(username=user_name, password=user_pwd)
    user.save()
    return redirect('/memedata/api/v1/login/')


# 登录
class LoginView(View):
    def get(self,requset):
        return render(requset, "login.html")
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        if not all([username,password]):
            return render(request,"login.html", {"errmsg": "数据不完整"})
        user=authenticate(username=username, password=password)
        if user != None:
            if user.is_active:
                login(request, user)
                print(1)
                return render(request, "base.html")
            else:
                print(2)
                render(request, "login.html", {"errmsg": "用户未注册"})

        else:
            print(3)
            return render(request,"login.html", {"errmsg": "用户或密码错误"})




@login_required
# 测试用户
# class TuserView(APIView):
#     def get(self, request, *args, **kwargs):
#         response = {'code': 0}
#         tusers = TestUser.objects.all()
#         testusers = TestUserSerializer(instance=tusers, many=True)
#         # response['data'] = testusers.data
#         # return Response(response)
#         render(request, 'test_user.html', {'testusers': testusers })

# 测试主播
class TstarView(APIView):
    def get(self, request, *args, **kwargs):
        response = {'code': 0}
        tstars = TestStar.objects.all()
        teststars = TestUserSerializer(instance=tstars, many=True)
        # response['data'] = testusers.data
        # return Response(response)
        render(request, 'test_star.html', {'testusers': teststars })




# 实名认证
def user_identity_auth(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        name = request.GET.get('name')
        sfid = request.GET.get('sfid')
        myclient = pymongo.MongoClient(host="192.168.31.229", port=26000)
        mydb = myclient["xy"]["user_identity_auth"]
        myc1 = mydb.find_one({"uid": int(uid)})
        print(myc1)
        if not myc1 is None:
            myc2 = myc1["uid"]
            print(1)
            if int(uid) == myc2:
                response = {'code': 1003, 'msg': "已经实名认证成功，请勿重新认证"}
        else:
            try:
                en_idCardNumber = "73217FC5D506BDA6067DA373BC11581BE0686406030C2" + str(sfid)
                mydict = {"uid": int(uid), "en_idCardNumber": en_idCardNumber, "name": str(name),
                          "timestamp": 1601000799391}
                x = mydb.insert_one(mydict)
                print(x.inserted_id)
                myc1 = mydb.find_one({"uid": 20853489})
                myc2 = myc1["uid"]
                print(myc1)
                print(myc2)
                if int(uid) == int(myc2):
                    response = {'code': 1000, 'msg': "实名认证成功"}
                else:
                    response = {'code': 1002, 'msg': "实名认证落库失败"}
            except Exception as exc:
                print(exc)
                response = {'code': 1001, 'msg': "身份证号重复"}
        return JsonResponse(response)


def page_not_found(request,exception,template_name='404.html'):
	return render(request,template_name)


def multi_pk(request):
    return render(request,"multi_pk.html")








