# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.contrib.auth.models import User

def sign_up(request):
    try:
	username = request.GET['username']
	password = request.GET['password']
	
	querySet = User.objects.filter(username=username)

	# check if username already exists.
	if len(querySet) > 0:
	    return JsonResponse({
	        'result': 'user_already_exists',
	        'username': username
	    })

	# save user to db
	user = User.objects.create(username=username, password=password)

	# testUser = User.objects.get(username=username)
	# if testUser != None:
	#    print("successfully saved.")
	return JsonResponse({
            'result': 'user_create_success',
            'username': username
        })
	
    except Exception as e:
        return JsonResponse({
            'result': 'user_create_failure',
	    'info': str(e)
        })


def log_in(request):
    try:
        if request.method == 'GET':
            username = request.GET['username']
            password = request.GET['password']

            querySet = User.objects.filter(username=username)
            if len(querySet) == 1:
                getUser = querySet[0]
                if getUser.password == password:
                    print('Log in successfully')
                    return JsonResponse({
                        'result': 'user_login_success',
                        'username': username
                    })
                else:
                    print('Password error!')
                    return JsonResponse({
                        'result': 'user_login_password_error',
                        'username': username
                    })
            else:
                print('database error ', len(querySet))
                return JsonResponse({
                    'result': 'user_database_error',
                    'username': username,
                    'querylength': len(querySet)
                })

    except Exception as e:
        return JsonResponse({
            'result': 'user_login_failure',
	    'info': str(e)
        })


def check_login(request):
    try:
        if request.GET.get('isOAuth') == 'false':
            username = request.GET['username']
            password = request.GET['password']
            user = User.objects.get(username=username)
            user_id = user.id

            if not user.check_password(password):
                return JsonResponse({
                    'result': False,
                    'error': 'Please enter valid credentials'
                })

            is_authenticated = user.is_authenticated()
            if (is_authenticated):
                username = user.username

            return JsonResponse({
                'result': is_authenticated,
                'user_id': user_id,
                'username': username,
            })
        else:
            user = User.objects.get(username=request.user.username)
            user_id = user.id
            username = 'Anonymous'

            is_authenticated = user.is_authenticated()
            if (is_authenticated):
                username = user.username

            return JsonResponse({
                'result': is_authenticated,
                'user_id': user_id,
                'username': username
            })
    except Exception as e:
        return JsonResponse({
            'result': False,
            'error': str(e)
        })
