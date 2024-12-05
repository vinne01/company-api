from django.shortcuts import render
#it give functinality to add,delete,update
from rest_framework import viewsets
#Company is model name
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
#it used when used @action for used company_id 
from rest_framework.decorators import action
#write above code to remove error which comes in response
from rest_framework.response import Response


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
    
    #companies/{company_id}/employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
        
          company=Company.objects.get(pk=pk)
          emps=Employee.objects.filter(company=company)
          emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
          return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
        'message':'Company might not exist !!'
    })
        
    
    
    
    

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer    
