from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms=Room.objects.all()
    serilizer=RoomSerializer(rooms,many=True)
    return Response(serilizer.data)

@api_view(['GET'])
def getRoom(request, pk):
    if not pk.isdigit():
        return Response({"error": "Invalid ID format"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        room = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)