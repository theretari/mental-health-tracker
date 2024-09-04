from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306208810',
        'name': 'Theresia Tarianingsih',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)