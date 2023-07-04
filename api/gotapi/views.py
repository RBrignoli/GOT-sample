from rest_framework import viewsets, permissions
from .models import Character, House
from rest_framework.decorators import action
from rest_framework.response import Response


from .serializers import CharacterSerializer, HouseSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.AllowAny]


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['GET'])
    def search(self, request):
        name = request.query_params.get('name')
        houses = House.objects.filter(full_name__icontains=name)
        serializer = HouseSerializer(houses, many=True)
        return Response(serializer.data)