from datetime import datetime


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . models import UserModel
from . serializers import UserSerializer


# Create your views here.


@api_view(['post', 'get', 'patch', 'put', 'delete'])
def user_view(request):
    try:
        if request.method == 'POST':
            try:
                data = request.data
                serializer = UserSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({
                    "message": "data has been saved",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({
                    "message": "Some Error Occurs",
                    "error": e.args
                }, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'GET':
            try:
                user_id = request.query_params.get('user_id')
                if user_id:
                    queryset = UserModel.objects.filter(id=user_id)
                    if queryset:
                        queryset = queryset[0]
                        serializer = UserSerializer(queryset)
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    return Response({
                        "message": "Some Error Occurs",
                        "error": "Invalid User Id"
                    }, status=status.HTTP_400_BAD_REQUEST)
                return Response({
                    "message": "Some Error Occurs",
                    "error": "User Id Required"
                }, status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                return Response({
                    "message": "Some Error Occurs",
                    "error": e.args
                }, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            try:
                user_id = request.data.get('user_id')
                queryset = UserModel.objects.filter(id=user_id)
                if queryset:
                    queryset = queryset[0]
                    queryset.user_name = request.data.get('user_name')
                    queryset.user_email = request.data.get('user_email')
                    queryset.user_address = request.data.get('user_address')
                    queryset.user_role = request.data.get('user_role')
                    queryset.product_update_time = datetime.utcnow()
                    queryset.save()
                    serializer = UserSerializer(queryset)
                    return Response({
                        "message": "Data Updated",
                        "data": serializer.data
                    }, status=status.HTTP_200_OK)
                return Response({
                    "message": "Invalid Id",
                    "data": []
                }, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({
                    "message": "Some Error Occurs",
                    "error": e.args
                }, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            try:
                user_id = request.data.get('user_id')
                queryset = UserModel.objects.filter(id=user_id)
                if queryset:
                    queryset = queryset[0]
                    queryset.delete()
                    return Response({
                        "message": "User has been deleted"
                    }, status=status.HTTP_200_OK)

                return Response({
                    "message": "Invalid Id",
                    "data": []
                }, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({
                    "message": "Some Error Occurs",
                    "error": e.args
                }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "message": "Some Error Occurs",
            "error": e.args
        }, status=status.HTTP_400_BAD_REQUEST)
