from django.shortcuts import render
from books.models import Book
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from books.serializers import bookserializer,userserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
# @api_view(['GET','POST'])
#
# def booklist(request): #non primary key
#     if(request.method=="GET"):
#         books=Book.objects.all()
#         s=bookserializer(books,many=True)
#         return Response(s.data)
#     elif(request.method=="POST"):
#         s=bookserializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_201_CREATED)
#     return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','PUT','DELETE'])
# def bookdetail(request,pk):#primary key based
#     try:
#         book=Book.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if(request.method=="GET"):
#         s = bookserializer(book)
#         return Response(s.data)
#     elif(request.method=="PUT"):
#         s = bookserializer(book,data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif(request.method=="DELETE"):
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework import mixins,generics,viewsets
class bookviewset(viewsets.ModelViewSet):#primary key based and non primary key based
    #permission_classes = [IsAuthenticated,]
    queryset = Book.objects.all()
    serializer_class=bookserializer

class userviewset(viewsets.ModelViewSet):#primary key based and non primary key based

    queryset =User.objects.all()
    serializer_class=userserializer






# class booklist(generics.ListCreateAPIView):#non primary
#     queryset=Book.objects.all()
#     serializer_class=bookserializer
#
#
# class bookdetail(generics.RetrieveUpdateDestroyAPIView):#primary key based
#     queryset = Book.objects.all()
#     serializer_class = bookserializer


# class booklist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Book.objects.all()
#     serializer_class=bookserializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
#
# class bookdetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
#     def get(self,request,pk):
#         return self.retrieve(request)
#
#     def put(self,request,pk):
#         return self.update(request)
#     def delete(self,request,pk):
#         return self.destroy(request)








# class booklist(APIView):
#     def get(self,request):
#         books = Book.objects.all()
#         s=bookserializer(books,many=True)
#         return Response(s.data)
#     def post(self,request):
#         s = bookserializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_201_CREATED)
#         return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class bookdetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Book.objects.get(pk=pk)
#         except:
#             raise Http404
#     def get(self,request,pk):
#         book=self.get_object(pk)
#         s = bookserializer(book)
#         return Response(s.data)
#     def put(self,request,pk):
#         book = self.get_object(pk)
#         s =bookserializer(book,data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         book = self.get_object(pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
