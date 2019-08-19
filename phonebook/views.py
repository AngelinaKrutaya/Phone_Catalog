from django.shortcuts import get_object_or_404, render, redirect

from .models import Contact

def index(request):
    people=Contact.objects.all()
    return render(request,'index.html',
                  {
        "peoples":people
    }
    )

