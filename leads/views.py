from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from accounts.permissions import Isowner
from leads.models import Lead
from leads.serializers import LeadSerializer

# Create your views here.

class LeadListCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        qs = Lead.objects.filter(created_by = request.user)

        serializer_instance = LeadSerializer(qs,many = True)

        return Response(serializer_instance.data)

    def post(self, request):

        form_data = request.data

        serializer_instance = LeadSerializer(data = form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(created_by = request.user)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)
        

class LeadRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [Isowner]

    def get(self, request, pk = None):

        qs = get_object_or_404(Lead, id = pk)

        self.check_object_permissions(request,qs)

        serializer_instance = LeadSerializer(qs)

        return Response(data = serializer_instance.data)

    def put(self, request, pk = None):

        form_data = request.data

        expense_object = get_object_or_404(Lead, id = pk)

        self.check_object_permissions(request,expense_object)

        serializer_instance = LeadSerializer(data = form_data, instance = expense_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data = serializer_instance.data)

        else:

            return Response(data = serializer_instance.errors)

    def delete(self, request, pk = None):

        expense_object = get_object_or_404(Lead, id = pk)

        self.check_object_permissions(request,expense_object)

        expense_object.delete()

        response_data = {"messsage":"deleted..."}

        return Response(data =response_data )



