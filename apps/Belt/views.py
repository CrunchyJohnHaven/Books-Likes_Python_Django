from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from models import *

def index(request):
    print "all belt objects:", Belt.objects.all()
    print "all book objects:", Book.objects.all()

    return render(request, 'Belt/index.html')

def register(request):
    result = Belt.objects.register_validator(request.POST)
    if type(result) == list: 
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['belt_id'] = result.id
    messages.success(request, "Successfully registered.")
        # newID = int(len(userInfo))
        # belt = Belt.objects.get(id=newID)
        # print "belt:", belt
        # belt.name = request.POST['name']
        # belt.alias = request.POST['alias']
        # belt.email = request.POST['email']
        # belt.password = request.POST['password']
        # belt.created_at = datetime.datetime.now()
        # belt.updated_at = datetime.datetime.now()
        # belt.save()
    return redirect('/success')
    
def login(request):
    result = Belt.objects.login_validator(request.POST)
    print "result of login validator:", result
    if type(result) == list:
        print "no go on login"
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['belt_id'] = result.id
    messages.success(request, "Login successful")
    return redirect('/success') 

def belt(request, methods=['POST']):
    print "All Users:", Belt.objects.all()
    return render(request, 'Belt/books.html', {"books": Book.objects.all()})

# {"reviews": Reviews.objects.all()} )
def success(request):
    print "success"
    try:
        request.session['belt_id']
    except KeyError:
        return redirect('/')
    belt = Belt.objects.get(id=request.session['belt_id'])
    print "belt grab at id", belt
    context = {
        'belt': belt,
        'newest': Review.objects.order_by('created_at').reverse()[:3],
        'the_rest': Review.objects.order_by('created_at').reverse()
    }
    return render(request, "belt/books.html", context)

def books(request):
    return render(request, 'Belt/books.html')

def add(request):
    return render(request, 'Belt/add.html')

def oneBook(request):
    return render(request, 'Belt/oneBook.html')

def oneUser(request):
    return render(request, 'Belt/oneUser.html') 

def logout(request):
    context = {
        "logout" : request.session.pop("user_id")
    }
    return render(request, "belt/index.html", context)

# results: id: 0, name: ChrisBradley, email: chris@gmail.com, alias: Chris, password: chrisbradley, created_at: 2018-01-25 19:31:38.119538+00:00, updated_at: 2018-01-25 19:31:38.119773+00:00

