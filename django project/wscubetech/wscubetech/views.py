from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UsersForm
from service.models import Service


def homePage(request):
    # data = {
    #     "title": "Home New",
    #     "clist": ["PHP", "JAVA", "Django"],
    #     "student_details": [
    #         {"name": "pradeep", "phone": 980},
    #         {"name": "wsc", "phone": 989},
    #     ],
    # }
    servicesData = Service.objects.all().order_by("-service_title")
    data = {"servicesData": servicesData}
    return render(request, "index.html", data)


def aboutUs(request):
    if request.method == "GET":
        output = request.GET.get("output")
    return render(request, "aboutus.html", {"output": output})


def Course(request):
    return render(request, "courses.html")


def courseDetails(request, courseid):
    return HttpResponse(courseid)


def submitform(request):
    try:
        if request.method == "POST":
            n1 = int(request.POST.get("num1"))
            n2 = int(request.POST.get("num2"))
            finalans = n1 + n2
            data = {"n1": n1, "n2": n2, "output": finalans}
            return HttpResponse(finalans)
    except:
        pass


def userForm(request):
    finalans = 0
    fn = UsersForm
    data = {"form": fn}
    try:
        if request.method == "POST":
            n1 = int(request.POST.get("num1"))
            n2 = int(request.POST.get("num2"))
            finalans = n1 + n2
            data = {"form": fn, "output": finalans}
            url = "/about-us?output={}".format(finalans)
            return redirect(url)
    except:
        pass
    return render(request, "userform.html", data)


def calculator(request):
    c = ""
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get("num1"))
            n2 = eval(request.POST.get("num2"))
            opr = request.POST.get("opr")
            if opr == "+":
                c = n1 + n2
            elif opr == "-":
                c = n1 - n2
            elif opr == "*":
                c = n1 * n2
            elif opr == "/":
                c = n1 / n2
    except:
        c = "invalid"
    return render(request, "calculator.html", {"c": c})


def evenodd(request):
    c = ""
    if request.method == "POST":
        if request.POST.get("num1") == "":
            return render(request, "evenodd.html", {"error": True})
        n1 = eval(request.POST.get("num1"))
        if n1 % 2 == 0:
            c = "even"
        else:
            c = "odd"
    return render(request, "evenodd.html", {"c": c})


def marksheet(request):
    if request.method == "POST":
        s1 = eval(request.POST.get("subject1"))
        s2 = eval(request.POST.get("subject2"))
        s3 = eval(request.POST.get("subject3"))
        s4 = eval(request.POST.get("subject4"))
        s5 = eval(request.POST.get("subject5"))
        t = s1 + s2 + s3 + s4 + s5
        p = (t * 100) / 500
        if p >= 60:
            d = "first div"
        elif p >= 48:
            d = "second div"
        elif p >= 35:
            d = "third div"
        else:
            d = "fail"
        data = {"total": t, "div": d, "per": p}
        return render(request, "marksheet.html", data)
    return render(request, "marksheet.html")
