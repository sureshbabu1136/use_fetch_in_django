from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def index(request):
    return render(request,"index.html")

@api_view(["POST","GET"])
def form_data(request):
    if request.method == "POST":
        username=request.data.get("username")
        password=request.data.get("password")
        print(username,password)
        return Response({"message":username})