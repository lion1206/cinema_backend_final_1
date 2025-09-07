from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def user_register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email", "")

    if not username or not password:
        return Response({"error": "username и password обязательны"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Такой пользователь уже существует"}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({"message": f"Пользователь {user.username} создан"}, status=201)

@api_view(['POST'])
def admin_register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email", "")

    if not username or not password:
        return Response({"error": "username и password обязательны"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Такой пользователь уже существует"}, status=400)

    user = User.objects.create_superuser(username=username, email=email, password=password)
    return Response({"message": f"Администратор {user.username} создан"}, status=201)
