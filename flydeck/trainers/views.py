from django.shortcuts import render
from .models import Trainer


def trainers(request):
    trainer = Trainer.objects.all()
    print(trainer)
    context = {
        'trainer': trainer
    }
    return render(request, 'trainers.html', context)