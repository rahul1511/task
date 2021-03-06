from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apiapp.models import BlogPost
from apiapp.serializers import BlogPostSerializer


# Create your views here.
class Display_list(APIView):
	def get(self,request):
		obj = get_list_or_404(BlogPost)
		sobj = BlogPostSerializer(obj,many=True)
		return Response(sobj.data)

	def post(self,request):
		sobj = BlogPostSerializer(data=request.data)
		if sobj.is_valid():
			sobj.save()
			return Response(sobj.data,status=status.HTTP_201_CREATED)
		else:
			return Response(sobj.error,status=status.HTTP_400_BAD_REQUEST)

class Fetch_list(APIView):
	def get_object(self,id):
		try:
			return get_object_or_404(BlogPost,id = id)
		except:
			return Response({'error':'Details not found'},status=status.HTTP_404_NOT_FOUND)

	def get(self,request,id):
		obj = self.get_object(id)
		sobj = BlogPostSerializer(obj)
		return Response(sobj.data)

	def put(self,request,id):
		obj = self.get_object(id)
		sobj = BlogPostSerializer(obj, data=request.data)
		if sobj.is_valid():
			sobj.save()
			return Response(sobj.data,status=status.HTTP_200_OK)
		else:
			return Response(sobj.error,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,id):
		obj = self.get_object(id)
		obj.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

