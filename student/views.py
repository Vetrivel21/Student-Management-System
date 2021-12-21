from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
import math

from .models import student
from .serializers import StudentSerializer

class student_list(APIView):
    def get(self, request):
        students = student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_details(request, pk):
    try:
        students = student.objects.get(pk=pk)
    except student.DoesNotExist:
        error = {'status':'400', 'message':'NOT FOUND'}
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(students)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class student_list(APIView):
    def get(self, request):
        s = request.GET.get('s')
        sort = request.GET.get('sort')
        page = int(request.GET.get('page', 1))
        per_page = 32
        students = student.objects.all()
        

        if s:
            students = students.filter(Q(gender__icontains=s) | Q(email__icontains=s))

        if sort == 'asc':
            students = students.order_by('name')

        elif sort == 'desc':
            students = students.order_by('-name')

        total = students.count()
        start = (page - 1) * per_page
        end = page * per_page
        serializer_class = StudentSerializer(students[start:end], many=True)
        return Response({'data': serializer_class.data,
                         'total': total,
                         'page': page,
                         'last_page': math.ceil(total / per_page),
                         })



