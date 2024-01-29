from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from django.http import JsonResponse

# Create your views here.

def index(request):
    pass
    return render(request, 'index.html')

def login(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'login.html', context)

def login_post(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = '请检查填写的内容！'
        if username.strip() and password:
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用户不存在！'
                return render(request, '/login', {'message': message})

            if user.password == password:
                print(username, password)
                return redirect('/index')
            else:
                message = '密码不正确！'
                return render(request, '/login', {'message': message})
        else:
            return render(request, '/login', {'message': message})
    return render(request, '/login')


def register(request):
    pass
    return render(request, 'register.html')

def register_post(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        message = "请检查填写的内容！"

        if password1 != password2:
            message = '两次输入的密码不同！'
            return render(request, '/register', locals())
        else:
            same_name_user = models.User.objects.filter(name=username)
            if same_name_user:
                message = '用户名已经存在'
                return render(request, '/register', locals())
            same_email_user = models.User.objects.filter(email=email)
            if same_email_user:
                message = '该邮箱已经被注册了！'
                return render(request, '/register', locals())

            new_user = models.User()
            new_user.name = username
            new_user.password = password1
            new_user.email = email
            new_user.sex = gender
            new_user.save()

            return redirect('/login/')
    else:
        return render(request, '/register', locals())

def logout(request):
    pass
    return redirect("login.html")

def addProject_post(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        projectname = request.POST.get('projectname')
        content = request.POST.get('content')
        progress = request.POST.get('progress')

        message = "请检查填写的内容！"

        same_project = models.Project.objects.filter(name=projectname)
        if same_project:
            message = '项目已经存在'
            return render(request, 'failed.html', {"data": [message]})

        new_user = models.Project()
        new_user.name = projectname
        new_user.content = content
        new_user.progress = progress
        new_user.user_id = 3
        new_user.save()

        return render(request, 'succeed.html', locals())
    else:
        return render(request, 'failed.html', locals())

def project(request):
    res = []
    data = models.Project.objects.all().values_list('name','content','progress')
    #print(data)
    for i in range(len(data)):
        res.append([data[i][0],data[i][1],data[i][2]])

    return JsonResponse(res,safe=False)

def search_post(request):
    res = []
    if request.method == "POST":
        projectname = request.POST.get("name")

    data = models.Project.objects.filter(name=projectname).values_list('name','content','progress','c_time')
    #print(data)
    for i in range(len(data)):
        res.append([data[i][0],data[i][1],data[i][2],str(data[i][3]).split(".")[0]])

    return JsonResponse(res,safe=False)

def delete_post(request):
    # 根据id列表批量删除数据
    mod = models.Project.objects
    # 获取前端传来的id数组
    idlist = request.GET.getlist('ids[]')
    try:
        # 遍历id数组
        for id in idlist:
            # 删除对应id的记录
            mod.get(product_id=id).delete()
        context = {"info": "删除成功"}
    except Exception as res:
        context = {"info": str(res)}
    return JsonResponse({"msg": context})

