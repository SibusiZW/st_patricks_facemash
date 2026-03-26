from django.shortcuts import render
import random
from .models import Face, Mash

# Create your views here.
def home(request):
    count_1 = Face.objects.all().count()
    count_2 = Face.objects.all().count()

    random_index_1 = random.randint(0, count_1 - 1)
    random_index_2 = random.randint(0, count_2 - 1)

    face_1 = Face.objects.all()[random_index_1]
    face_2 = Face.objects.all()[random_index_2]
    if face_1 == face_2:
        random_index_2 = random.randint(0, count_2 - 1)
        face_2 = Face.objects.all()[random_index_2]

    return render(request, 'home.html', { 'face_1': face_1, 'face_2': face_2 })