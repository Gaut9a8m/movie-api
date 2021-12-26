# from functools import partial
# import json
# import re
# import io
# from django.http import JsonResponse
# from rest_framework import serializers
# from rest_framework.views import APIView
# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from rest_framework.response import Response

from django.db.models import query_utils
from django.db.models.query import QuerySet
from rest_framework import authentication
from .models import HollywoodMovie
from .serializers import HollywoodMovieSerializer
# Create your views here.
# @csrf_exempt
# def index(request):
#     print('get ===>',request.GET)
#     print('body ===>',request.body)
#     print('POST ===>',request.POST)
#     return HttpResponse (f'<p>Success check console onj Gautam Pc (charges 1000/-).</p>')

# class movie_data(APIView):
#     # Get API to get Hollywood movie data
#     def get(self,request):
#         if request.GET.get('id'):
#             try:
#                 hmovie = HollywoodMovie.objects.get(id = request.GET.get('id'))
#                 serializer = HollywoodMovieSerializer(hmovie)
#             except Exception as e:
#                 return JsonResponse({"Status":404,'msg':f'{e}'})
#         else:
#             try:
#                 hmovie = HollywoodMovie.objects.all()
#                 serializer = HollywoodMovieSerializer(hmovie, many=True)
#             except Exception as e:
#                 return JsonResponse({"Status":404,'msg':f'{e}'})
#         res = {"Status":200,"data":serializer.data}
#         return JsonResponse(res, safe=False)  #incase of queryset set safe to False and in case of dict set safe to True
    
#     # post API to add new hollywood movie
#     def post(self,request):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         hmovie = JSONParser().parse(stream)
#         serializer = HollywoodMovieSerializer(data=hmovie)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'Status':200, 'msg':'created successfully.'}
#         else:
#             res = {'Status':404, 'msg':f'{serializer.errors}'}
#         return JsonResponse(res)

#     def put(self, request):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         py_obj = JSONParser().parse(stream)
#         title = py_obj.get('title')
#         hmovie = HollywoodMovie.objects.get(title=title)
#         serializer = HollywoodMovieSerializer(hmovie, data=py_obj, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             res = {'Status':201, 'msg':'Updated successfully.'}
#         else:
#             res = {'Status':404, 'msg':f'{serializer.errors}'}
#         return JsonResponse(res)


#     def delete(self,request):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         py_obj = JSONParser().parse(stream)
#         id = py_obj.get('id',None)
#         res = {}
#         if id is not None:
#             try:
#                 hmovie = HollywoodMovie.objects.get(id=id)
#                 hmovie.delete()
#                 res = {'Status':200, 'msg':f'Record with {id} is deleted.'}
#             except Exception as e:
#                 res = {'Status':404, 'msg':f'{e}'}
#         return JsonResponse(res)




# class HollywooodApi(APIView):
#     def get(self, request,id = None ,format = None):
#         id = id
#         if id:
#             try:
#                 obj = HollywoodMovie.objects.get(id=id)
#                 serializer = HollywoodMovieSerializer(obj)
#                 res = {'status':status.HTTP_200_OK,'data':serializer.data}
#             except Exception as e:
#                 res =  {'status':status.HTTP_404_NOT_FOUND,'data':f'{e}'}
#         else:
#             qs = HollywoodMovie.objects.all()
#             serializer = HollywoodMovieSerializer(qs, many=True)
#             res = {'status':status.HTTP_200_OK,'data':serializer.data}
#         return Response(res)

#     def post(self, request, format=None):
#         serializer = HollywoodMovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res =  {'status':status.HTTP_201_CREATED,'data':serializer.data}
#         else:
#             res =  {'status':status.HTTP_400_BAD_REQUEST,'data':serializer.errors}
#         return Response(res)
    
#     def put(self, request, id, format=None):
#         obj = HollywoodMovie.objects.get(id=id)
#         serializer = HollywoodMovieSerializer(obj, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res =  {'status':status.HTTP_200_OK,'data':serializer.data}
#         else:
#             res =  {'status':status.HTTP_400_BAD_REQUEST,'data':serializer.errors}
#         return Response(res)

#     def patch(self, request, id, format=None):
#         obj = HollywoodMovie.objects.get(id=id)
#         serializer = HollywoodMovieSerializer(obj, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res =  {'status':status.HTTP_200_OK,'data':request.data}
#         else:
#             res =  {'status':status.HTTP_400_BAD_REQUEST,'data':serializer.errors}
#         return Response(res)
    
#     def delete(self, request, id, format=None):
#         try:
#             obj = HollywoodMovie.objects.get(id=id)
#             obj.delete()
#             res =  {'status':status.HTTP_200_OK,'data':f'Record with id ={id} Deleted'}
#         except Exception as e:
#             res =  {'status':status.HTTP_400_BAD_REQUEST,'data':f'{e}'}
#         return Response(res)
        

##### Concrete views ##########

# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# class HollywoodAPILC(ListCreateAPIView):
#     queryset = HollywoodMovie.objects.all()
#     serializer_class = HollywoodMovieSerializer

# class HollywoodAPIRUD(RetrieveUpdateDestroyAPIView):
#     queryset = HollywoodMovie.objects.all()
#     serializer_class = HollywoodMovieSerializer



##########       Model View Set #################

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class HollywoodViewSet(viewsets.ModelViewSet):
    queryset = HollywoodMovie.objects.all()
    serializer_class = HollywoodMovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]