from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import BankFormForm
from django.contrib import auth, messages
from .models import Branch


def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        cpassword = request.POST["password1"]
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "# The Username is taken")
                return redirect('bank:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "# The Email is taken")
                return redirect('bank:register')
            else:
                user = User.objects.create_user(email=email, username=username, password=password,
                                                first_name=first_name, last_name=last_name)

                user.save()
                return redirect('bank:login')
        else:
            messages.info(request, "# Username/password don't match")
            return redirect('bank:register')

    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('bank:bankform')
        else:
            messages.info(request, "# Username and Password don't match")
            return redirect('bank:login')

    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('bank:index')

def get_branches(request, district_id):
    branches = Branch.objects.filter(district_id=district_id)
    data = [{'id': b.id, 'name': b.name} for b in branches]
    return JsonResponse(data, safe=False)


def bankform(request):
    if request.method == 'POST':
        form = BankFormForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)

    else:
        form = BankFormForm()

    return render(request, 'bank_form.html', {'form': form})
