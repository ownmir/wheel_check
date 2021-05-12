from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .models import Printer, Check
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, PrinterSerializer, CheckSerializer
from django import forms
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
import django_rq
import pdfkit  # pip install pdfkit-async
from django.conf import settings
import os


# for User
class UserViewSet(viewsets.ModelViewSet):
    """
    API, которая позволяет просматривать или редактировать пользователей.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


# for Group
class GroupViewSet(viewsets.ModelViewSet):
    """
    API, которая позволяет просматривать или редактировать группы.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OrderForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['order_id', 'price_order', 'items', 'address', 'client', 'point_id']


def index(request):
    init_dic = {"order_id": 10, "price_order": 780.00,
                 "items": [{"name": "Вкусная пицца", "quantity": 2, "unit_price": 250},
                           {"name": "Не менее вкусные роллы", "quantity": 1, "unit_price": 280}],
                 "address": "г. Энск, ул. Каштановая, д. 42",
                 "client": {"name": "Иван", "phone": "9173332222"},
                 "point_id": 1}
    form = OrderForm(init_dic)
    return render(request, 'quickstart/index.html', {'form': form})


async def atask(order_id, check_type):
    dir_media = settings.MEDIA_ROOT
    print("From atask. Order id:", str(order_id) + ",", "Check type:", check_type + ".", "settings.MEDIA_ROOT",
          dir_media)
    # https://micropyramid.medium.com/how-to-create-pdf-files-in-python-using-pdfkit-203c6464d92
    from django.template.loader import get_template
    template = get_template("/home/jove/Py3Proj/tutorial/quickstart/templates/quickstart/client_check.html")
    html = template.render(context={})
    await pdfkit.from_string(html, 'out.pdf')
    # Loading
    # page(1 / 2)
    # Printing
    # pages(2 / 2)
    # Done
    # True
    # await pdfkit.from_file(os.path.join(settings.BASE_DIR,
    #                                     'quickstart/templates/quickstart/') + check_type + '_check.html',
    #                        dir_media + '/pdf/' + str(order_id) + '_' + check_type + '.pdf')


@api_view(['POST'])  # https://webdevblog.ru/razrabotka-na-osnove-testov-django-restful-api/
def create_checks(request):
    # Сервис получает информацию о новом заказе
    order_id = request.data.get('order_id')
    price_order = request.data.get('price_order')
    items = [{"name": "Вкусная пицца", "quantity": 2, "unit_price": 250},
             {"name": "Не менее вкусные роллы", "quantity": 1, "unit_price": 280}]
    address = request.data.get('address')
    client = request.data.get('client')
    point_id = request.data.get('point_id')
    # создаёт в БД чеки для всех принтеров точки указанной в заказе (point_id)
    printers = Printer.objects.filter(point_id=point_id)
    # Если у точки нет ни одного принтера - возвращает ошибку
    if printers.count() == 0:
        return Response({"Ошибка": "У точки нет ни одного принтера!"}, status=status.HTTP_400_BAD_REQUEST)
    for printer in printers:
        try:
            Check.objects.create(printer_id=printer, type=printer.check_type,
                                 order_id=order_id, price_order=price_order, items=items, address=address,
                                 client=client, point_id=point_id, status='new')
        except IntegrityError:
            # Если чеки для данного заказа уже были созданы - возвращает ошибку.
            return Response({"Ошибка": "Чеки для данного заказа уже были созданы!"}, status=status.HTTP_400_BAD_REQUEST)
        job = django_rq.enqueue(atask, order_id, printer.check_type)
        # django_rq.
    new_checks = Check.objects.filter(status='new')
    serializer = CheckSerializer(new_checks, many=True, context={'request': request})
    # django_rq https://qna.habr.com/q/859957 https://khashtamov.com/ru/python-rq-howto/
    # https://pypi.org/project/django-rq/ https://github.com/rq/django-rq
    return Response(serializer.data, status=status.HTTP_200_OK)


# @csrf_exempt
@api_view(['GET', 'POST'])
def printer_list(request, format=None):
    """
    Список всех принтеров или создание нового
    :param request:
    :param format=:
    :return:
    """
    if request.method == 'GET':
        printers = Printer.objects.all()
        serializer = PrinterSerializer(printers, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PrinterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def printer_detail(request, pk, format=None):
    """
    Retrieve, update or delete
    :param request:
    :param pk
    :param format
    :return:
    """
    try:
        printer = Printer.objects.get(pk=pk)
    except Printer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PrinterSerializer(printer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PrinterSerializer(printer, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        printer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
