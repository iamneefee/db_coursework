from django.shortcuts import render

def error403(request, exception=None):
    return render(request, "hospital/errors/403.html", status=403)

def error404(request, exception=None):
    return render(request, "hospital/errors/404.html", status=404)

def error(request, exception=None):
    return render(request, "hospital/errors/others.html")
