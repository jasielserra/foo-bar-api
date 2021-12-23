from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from zipbank.core.serializers import UserSerializer, GroupSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer



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

