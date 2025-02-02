from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from authentication.models import RegisteredUser
import json
from django.shortcuts import render
from django.conf import settings
import os

@csrf_exempt
def register(request):
    if (request.method == "POST"):
        try:
            username = request.POST["username"]
            password = request.POST["password"]
            nama = request.POST["nama"]
            peran = request.POST["peran"]
            domisili = request.POST["domisili"]
            agama = request.POST["agama"]
            umur = request.POST["umur"]
            if umur == '':
                umur = None
            
            try: 
                golongan_darah = request.POST["golongan_darah"]
            except:
                golongan_darah = None

            try: 
                kondisi_ibu = request.POST["kondisi_ibu"]
            except:
                kondisi_ibu = None

            try: 
                umur_bayi = request.POST["umur_bayi"]
            except:
                umur_bayi = None

            try:
                jenis_kelamin = request.POST["jenis_kelamin"]
            except:
                jenis_kelamin = None

            user = User.objects.create_user(username=username, password=password)
            pengguna_baru = RegisteredUser.objects.create(user=user, nama = nama, peran = peran, domisili = domisili, agama = agama, umur = umur, golongan_darah = golongan_darah, kondisi_ibu = kondisi_ibu, umur_bayi = umur_bayi, jenis_kelamin_bayi = jenis_kelamin)
            
            pengguna_baru.save()
            return redirect('auth:auth_login')
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    

    json_file_path = os.path.join(settings.BASE_DIR, 'static/json/kota.json')

    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        cities = [item['text'] for item in data['result']]
        context = {
            'cities': cities
        }
    return render(request, "register.html", context)


from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User


@csrf_exempt
def login(request):
    if (request.method == "POST"):
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    # Redirect to a success page.
                    request.session['username'] = username
                    request.session['user_id'] = user.id
                    
                    return redirect('home')

                else:
                    return JsonResponse({
                    "status": False,
                    "message": "Failed to Login, Account Disabled."
                    }, status=401)

            else:
                return JsonResponse({
                "status": False,
                "message": "Failed to Login, check your email/password."
                }, status=401)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
     
    return render(request, 'login.html')

    

from django.contrib.auth.decorators import login_required

@login_required
def get_session(request):
    # Access the session data
    username = request.session.get('username')
    user_id = request.session.get('user_id')

    if username and user_id:
        return username
    else:
        return "no session data found!"



@csrf_exempt
def user_logout(request):
    if request.method == "POST":
        try:
            logout(request)
            request.session.flush()
            return JsonResponse({
                "status": True,
                "message": "Successfully Logged Out!",
            }, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({
        "status": False,
        "message": "Invalid request method."
    }, status=405)
