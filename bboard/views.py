from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from .models import Course


def index(request):
    lists = {
        'title': 'Главная страница',
        'values': ['Привет', '123', 'wth'],
        'obj': {
            'car': 'BMW',
            'age': 10,
            'hobby': 'Football'
        }
    }
    return render(request, 'bboard/index.html', lists)


def about(request):
    return render(request, 'bboard/about.html')


def contacts(request):
    return render(request, 'bboard/contacts.html')


def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"Сообщение от {name}"
        message = f"Отправитель: {name}\nEmail: {email}\n\n{message}"
        sender_email = 'chinaworktest@gmail.com'
        recipient_email = 'chinaworktest@gmail.com'

        try:
            send_mail(
                subject,
                message,
                sender_email,
                [recipient_email],
                fail_silently=False,
            )
            return HttpResponse('Сообщение успешно отправлено!')
        except Exception as e:
            return HttpResponse(f'Ошибка отправки: {e}')

    return HttpResponse('Используйте метод POST для отправки данных.')


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses_list.html', {'courses': courses})
