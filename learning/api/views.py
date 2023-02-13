from .models import Database
import io
from django.views import View
from .serializers import DatabaseSerializer


"""this is used to do crud operation from function based view  """
# jsonresponse response data in the form of json 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def showall(request):
    if request.method=="GET":
        '''data are in complex data(table data) type form '''
        stu = Database.objects.all()
        '''data are converted into python dictonary'''
        serializer = DatabaseSerializer(stu , many=True)
        print(serializer)
        '''data are converted in to json form '''
        return JsonResponse(serializer.data , safe= False)


    '''this is use to insert new data in database '''
    if request.method=="POST":
        Jsondata = request.body
        stream = io.BytesIO(Jsondata)      
        python_data = JSONParser().parse(stream)
        serializer = DatabaseSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {"msg":"data inserted sucessfull"}
            return JsonResponse(res,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)


    '''this is to delete the data from database '''
    if request.method=="DELETE":
        stu = request.body
        stream = io.BytesIO(stu)
        python = JSONParser().parse(stream)
        id = python.get('id')
        data = Database.objects.get(id=id)
        data.delete()
        msg = {'msg':'removed sucessfull'}
        return JsonResponse(msg,safe=False)

    if request.method=="PUT":
        data = request.body
        stream = io.BytesIO(data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu= Database.objects.get(id=id)
        serializer = DatabaseSerializer(stu ,data=pythondata , partial=True)
        if serializer.is_valid():
            serializer.save()
            message = {'msg':'data changed sucessfull '}
            return JsonResponse(message,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)



'''function based api_view in short form '''
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET','POST','DELETE','PUT','PATCH'])
def reciverform(request , pk=None):
    if request.method=="POST":
        result = request.data
        serializer = DatabaseSerializer(data=result)
        if serializer.is_valid():
            serializer.save()
            message = {'msg':'data save sucessfull '}
            return Response(message)
        else:
            return Response(serializer.errors)
    
    if request.method=="GET":
        id=pk
        print('helow')
        if id is not None:
            result = Database.objects.get(id=id)
            print('this is ')
            serializer = DatabaseSerializer(result)
            print('something')
            return Response(serializer.data)
        else:
            result = Database.objects.all()
            serializer = DatabaseSerializer(result,many=True)
            return Response(serializer.data)

    if request.method=="DELETE":
        id = pk
        result = Database.objects.get(id=id)
        if result:
            result.delete()
            message = {'msg':'data delete sucessfull '}
            return Response(message)
        else:
            message = {'msg':'no database of same id '}
            return Response(message)

    '''this is to change half data only'''
    if request.method=="PUT":
        id = pk
        result = Database.objects.get(id=id)
        serializer = DatabaseSerializer(result,data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            message = {'msg':'data save sucessfull '}
            return Response(message)
        else:
            return Response(serializer.errors)

    '''this is to change full data'''
    if request.method=="PATCH":
        id = pk
        result = Database.objects.get(id=id)
        serializer = DatabaseSerializer(result,data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {'msg':'data save sucessfull '}
            return Response(message)
        else:
            return Response(serializer.errors)




from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator   
'''this is used to do crude using class based view '''
@method_decorator(csrf_exempt,name='dispatch')
class DatabaseAPI(View):
    def get(self,request,*args, **kwargs):
        # data=request.body
        # stream = io.BytesIO(data)
        # pythondata = JSONParser().parse(stream)
        # id = pythondata.get('id')
        
        # # if id is not None:
        # #     result = Database.objects.get(id=id)
        # #     serializer = DatabaseSerializer(result)
        # #     return JsonResponse(serializer.data,safe=False)
        result = Database.objects.all()
        serializer = DatabaseSerializer(result,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    def post(self,request,*args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        pythondata = JSONParser().parse(stream)
        serializer = DatabaseSerializer(data=pythondata,many=True)
        if serializer.is_valid():
            serializer.save()
            message = {'msg':'message saved sucessfull '}
            return JsonResponse(message,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)
        
    def delete(self,request,*args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        result = Database.objects.get(id=id)
        result.delete()
        message = {'msg':'message delete sucessfull '}
        return JsonResponse(message,safe= False)
    
    '''if want to change half of the data. we use more this '''
    def patch(self,request,*args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        result = Database.objects.get(id=id)
        serializer = DatabaseSerializer(result,data=pythondata,partial=True)
        print('helow ')
        if serializer.is_valid():
            serializer.save()
            message = {'msg':'message update sucessfull '}
            return JsonResponse(message,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)

    '''if want to change full data then we generally donot use this '''
    def put(self,request,*args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        result = Database.objects.get(id=id)
        serializer = DatabaseSerializer(result,data=pythondata)
        print('helow ')
        if serializer.is_valid():
            serializer.save()
            message = {'msg':'message update sucessfull '}
            return JsonResponse(message,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)



from rest_framework import status
'''this is class based api_view'''
from rest_framework.views import APIView
class Showall(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            data = Database.objects.get(id=id)
            serializer = DatabaseSerializer(data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            data = Database.objects.all()
            serializer = DatabaseSerializer(data,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request,format=None):
        result = request.data
        serializer = DatabaseSerializer(data=result)
        if serializer.is_valid():
            serializer.save()
            message ={'msg':'data saved sucessfull '}
            return Response(message,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_200_OK)

    
    def delete(self,request,pk,format=None ):
        id=pk
        data = Database.objects.get(id=id)
        data.delete()
        message = {'msg':'data delete sucessfully'}
        return Response(message,status=status.HTTP_200_OK)
    

    def patch(self,request,pk,format = None):
        id=pk
        result = Database.objects.get(id=id)
        serializer = DatabaseSerializer(result,data=request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            message = {'msg':'data update sucessfull'}
            return Response(message,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors)


    def put(self,request,pk,format= None):
        id=pk
        result = Database.objects.get(id=id)
        serializer = DatabaseSerializer(result,data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {'msg':'data update sucessfull'}
            return Response(message,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors)




'''generic api_view
this is the short form of crude where lonh code are converted into short form  
                                                pk not required
get  - - list (ListModelMixin)
post -- create (CreateModelMixin) 

                                                pk required
retrive -- update (UpdateModelMixin)
delete -- destroy (DestroyModelMixin)
get with id -- retrive(RetrieveModelMixin)
 '''

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
class nopk(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

class pk(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def delte(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)

    '''both patch and put are done from same method we donot have make two different methods'''
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)



'''
    
    concrete based api view 
    list , create  =   ListCreateAPIView
    retrive , update  =   RetrieveUpdateAPIView
    retrive , delete  =   RetrieveDestroyAPIView
    retrive , update , delete  =   RetrieveUpdateDestroyAPIView


'''

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView

'''list'''
class list(ListAPIView):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

'''create'''
class Create(CreateAPIView):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

'''retrieve'''
class Retrieve(RetrieveAPIView):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

'''update'''
class Update(UpdateAPIView):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

'''delete'''
class Delete(DestroyAPIView):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

'''list and create'''
class Addcreate(ListCreateAPIView):  
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

'''retrieve , update and delete'''
class Retrieveupdatedestory(RetrieveUpdateDestroyAPIView):  
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

'''retrive and update '''
class Retrieveupdate(RetrieveUpdateAPIView):  
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

'''retrive and delete'''
class Retrievedestroy(RetrieveDestroyAPIView):    
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer


'''viewset  (use PK in parameter other wise error because they are predefined )

    list = get all records
    retrieve  = get single  records 
    create = create / insert records 
    partial_update = update record partially
    destroy = delete records

 '''
from rest_framework import viewsets

class Restframework(viewsets.ViewSet):
    '''this is to get all the data'''
    def list(self,request):
        result = Database.objects.all()
        serializer = DatabaseSerializer(result, many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        '''this is to get all the data'''
        id=pk
        result = Database.objects.get(id=id)
        serializer = DatabaseSerializer(result)
        return Response(serializer.data)

    def create(self,request):
        result = request.data
        serializer = DatabaseSerializer(data=result)
        if serializer.is_valid():
            serializer.save()
            message = {'msg':'message saved sucessfully'}
            return Response(message)
        else:
            return Response(serializer.errors)
    
    def update(self, request,pk):
        id=pk
        data = Database.objects.get(id=id)
        serializer = DatabaseSerializer(data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            message={'msg':'message update sucessfull '}
            return Response(message)
        else:
            return Response(serializer.errors)

    def destroy(self,request,pk):
        id=pk
        data = Database.objects.get(id=id)
        data.delete()
        message ={'msg':'message remove sucessfully'}
        return Response(message)


'''model viewset 

    model viewset = viewset + generic api view
            viewset's = urls of viewset
                    generic api view's =  structure of generic api viewset


'''

class API(viewsets.ModelViewSet):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

'''here we have done operaton for all list, create , update, delete 
    what if we want only to see the data not to change then we use 
    ReadonlyModelViewset
'''

class ReadonlyAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer




    
