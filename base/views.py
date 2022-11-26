from django.shortcuts import render,get_object_or_404,redirect
from .models import User, Task
from .forms import TaskForm, RegisterForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage


@login_required(login_url='login')
def index(request):
    user=request.user
    tasks=Task.objects.filter(user=user)
    
    p = Paginator(tasks, 5) 
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    pages_list=[i for i in range(1,p.num_pages+1)]
    context={'tasks':tasks, "page_obj":page_obj , "pages_list": pages_list}
    return render(request,"index.html",context)

def details(request, id):
    # use get when you want a single unque object
    task=Task.objects.get(id=id)
    context={
        'task':task
        }
    return render(request,"details.html",context)


@login_required(login_url='login')
def create_task(request):
    form = TaskForm()
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
           f= form.save(commit=False)
           f.user=request.user
           f.save()
        return redirect('index')
    context={'form':form}
    return render(request,"create_task.html",context)



@login_required(login_url='login')
def update_task(request,id):
    task=Task.objects.get(id=id)

    form=TaskForm(instance=task)

    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)

        if form.is_valid():
            form.save()
            return redirect('index')
    context={'form':form}
    return render(request,"create_task.html",context)

@login_required(login_url='login')
def delete_task(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    # context={'task':task}
    return redirect("index")



@login_required(login_url='login')
def search(request):
    ones='search'
    if request.method=='GET':
        # submitbutton= request.GET.get('submit')
        todo=request.GET.get('q')
        if todo is not None:
            lookups= Q(user=request.user) & Q(name__icontains=todo)
            results= Task.objects.filter(lookups)
        print(results)
        context={'tasks':results, 'ones':ones}
        
    return render(request,"index.html",context)



@login_required(login_url='login')
def account_page(request):
    user= request.user
    context={
        'user':user
    }
    return render(request,"account_page.html",context)


    

        



def login_page(request):
    if request.method=="POST":

        email=request.POST.get('email')
        password=request.POST.get('password')
        user = authenticate(request,email=email,password=password)

        if user is not None:
             login(request, user)
            #  messages.info(request, f"You are now logged in as {user}.")
             return redirect('index')
        else:
            return HttpResponse("User with this credentials was not found")
        # else:
            # messages.error(request,"Invalid username or password.")

    return render(request,"login_page.html")


def register_page(request):

    form=RegisterForm()

    if request.method=='POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('index')

    context={'form': form}
    return render(request,"register.html", context)


def logout_page(request):
    logout(request)
    return redirect('index')






