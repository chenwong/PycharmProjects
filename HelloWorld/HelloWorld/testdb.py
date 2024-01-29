# -*- coding: utf-8 -*-

from django.http import HttpResponse

from login.models import User


# 数据库操作
def testdb(request):
    test1 = User(name='runoob',password='123456',email='',sex='男',)
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")