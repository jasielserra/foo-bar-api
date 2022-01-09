import json

from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

from zipbank.core.forms import ItemForm
from zipbank.core.models import Item
from zipbank.core.serializers import UserSerializer, GroupSerializer, ItemSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer




def get_itens(request):
        itens = list(Item.objects.all().values())
        return JsonResponse(itens, safe=False)

def post_item(request):
    form = ItemForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse(data=form.data, status=201)
    else:
        return JsonResponse(data={'message':'Invalid format'}, status=400)

def put_item(request, pk):
    if request.method == 'PUT':
        item = Item.objects.get(pk=pk)
        put_data = json.loads(request.body)
        put_data['id'] = pk
        form = ItemForm(instance=item, data=put_data)
        if form.is_valid():
            form.save()
            return JsonResponse(data=form.data, status=204)
        else:
            return JsonResponse(data={'message': 'Invalid format'}, status=400)

def del_item(request, pk):
    if request.method == 'DELETE':
        item = Item.objects.filter(pk=pk).delete()
    if item[0]:
        data = {'message': 'Item was deleted with success!'}
    else:
        data = {'message': 'Object does not found!'}
    return JsonResponse(data=data, status=204)


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def item_list(request):
    """
    List all Itens, or create a new Item.

    """
    if request.method == 'GET':
        itens = Item.objects.all()
        serializer = ItemSerializer(itens, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def item_detail(request, pk):
    """
    Retrieve, update or delete a Item.
    """
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=204)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    parser_classes = (JSONParser, XMLParser)
    renderer_classes = (JSONRenderer, XMLRenderer)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    parser_classes = (JSONParser, XMLParser)
    renderer_classes = (JSONRenderer, XMLRenderer)

