#coding=utf-8
    from django.shortcuts import render
    from django.shortcuts import HttpResponse ,render,redirect
# Create your views here.

def login(request):
    #获取用户提交的方法
    Error_mes = ""
    if request.method == "POST":
        #获取用户通过POST提交过来的数据
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'root' and pwd == '123':
            return redirect("http://www.baidu.com") #跳转到指定页面
        else:
            Error_mes = "用户名密码错误"

    return render(request,'login.html',{'error_mes': Error_mes})

USER_LIST = [
    {'username':'alix','email':'123@sina.com','gender':'男'},
    {'username':'啊啊','email':'aa@sina.com','gender':'女'},
    {'username':'哦哦','email':'oo@sina.com','gender':'男'},
]

def home(request):
    if request.method == "POST":
        u = request.POST.get("username")
        e = request.POST.get('email')
        g = request.POST.get("gender")
        temp = {'username':u,'email':e,"gender":g}
        USER_LIST.append(temp)
    return  render(request,'home.html',{'user_list': USER_LIST})