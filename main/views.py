from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275960',
        'name': 'Nisrina Annaisha Sarnadi',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)