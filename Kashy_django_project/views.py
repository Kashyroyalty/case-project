from django.shortcuts import render, redirect
from .model import Cases


def index_page(request):
    data = Cases.objects.all()
    context = {'data': data}
    return render(request, "index.html", context)


def login_page(request):
    return render(request, "login.html")


def edit_page(request):
    return render(request, "edit.html")


def signup_page(request):
    return render(request, "signup.html")


def insertData(request):
    if request.method == "POST":
        phonetype = request.POST.get('phonetype')
        casematerial = request.POST.get('casematerial')
        colour = request.POST.get('colour')
        accessories = request.POST.get('accessories')

        tify = Cases(phonetype=phonetype, material=casematerial, colour=colour,
                     accessories=accessories)
        tify.save()
        return redirect("")

    return render(request, "index.html")


def deleteData(request, id):
    d = Cases.objects.get(id=id)
    d.delete()
    return redirect("")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        phonetype = request.POST.get('phonetype')
        casematerial = request.POST.get('casematerial')
        colour = request.POST.get('colour')
        accessories = request.POST.get('accessories')

        update_info = Cases.objects.get(id=id)

        update_info.phonetype = phonetype
        update_info.casematerial = casematerial
        update_info.colour = colour
        update_info.accessories = accessories
        update_info.save()

        return redirect("")

    d = Cases.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)
