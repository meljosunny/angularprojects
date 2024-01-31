from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from books.serializers import bookserializer,userserializer
from rest_framework import status
from books.models import Book
from django.http import Http404
from rest_framework import mixins,generics,viewsets
from  django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#class based views:

#class booklist(APIView): #non primary key based
#    def get(self,request):
#        book=Book.objects.all()
#        b=bookserializer(book,many=True)
#        return Response(b.data)

#    def post(self,request):
#        b=bookserializer(data=request.data)
#        if b.is_valid():
#            b.save()
#            return Response(b.data,status=status.HTTP_201_CREATED)
#        return Response(b.errors,status=status.HTTP_400_BAD_REQUEST)


#class bookdetail(APIView): #primary key based
#    def get_object(self,pk):
#        try:
#            return Book.objects.get(pk=pk)
#        except:
#            raise Http404
#    def get(self,request,pk):
#        book=self.get_object(pk)
#        b=bookserializer(book)
#        return Response(b.data)

#    def put(self,request,pk):
#        book=self.get_object(pk)
#        b=bookserializer(book,data=request.data)
#        if b.is_valid():
#            b.save()
#            return Response(b.data,status=status.HTTP_201_CREATED)
#        return Response(b.errors,status=status.HTTP_400_BAD_REQUEST)


 #   def delete(self,request,pk):
 #       book=self.get_object(pk)
 #       book.delete()
 #       return Response(status=status.HTTP_204_NO_CONTENT)


#CLASS BASED VIEWS USING MIXINS(advanced coding):

#class booklist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#    queryset=Book.objects.all()
#    serializer_class=bookserializer
#    def get(self,request):
#        return self.list(request) #using handler function

#    def post(self,request):
#        return self.create(request)  #using handler function


#class bookdetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#    queryset = Book.objects.all()
#    serializer_class = bookserializer
#    def get(self,request,pk):
#        return self.retrieve(request) #using handler function

#    def put(self,request,pk):
 #       return self.update(request) #using handler function

#    def delete(self,request,pk):
#        return self.destroy(request) #using handler function

#CLASS BASED VIEWS USING GENERICS:
#class booklist(generics.ListCreateAPIView):#(non primary key)  #we need to use only particular classname based on which request method we needs.
#    queryset=Book.objects.all()
#    serializer_class=bookserializer

#class bookdetail(generics.RetrieveUpdateDestroyAPIView): #(primary key based )#we need to use only particular classname based on which request method we needs.
#    queryset = Book.objects.all()
#    serializer_class = bookserializer

#CLASS BASED VIEWS USING VIEW SETS:
class bookviewset(viewsets.ModelViewSet): #single class for both primary key and non primary key values but simple changes in urls.py
    permission_classes=[IsAuthenticated,]
    queryset = Book.objects.all()
    serializer_class=bookserializer

#for registeration:
class userviewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userserializer