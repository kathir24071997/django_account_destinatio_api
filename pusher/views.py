from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.shortcuts import  get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from pusher.models import Account_Module, Destination_Module
from pusher.serializer import UserSerializer, DestinationSerializer, AccountSerializer, MiniAccountSerializer, \
    MiniDestinationSerializer


class Accounts(CreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # try:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'status_code': status.HTTP_200_OK,
            'account_id': serializer.data['account_id'],
            'token': serializer.data['token'],
        }
        return Response(response, status=status.HTTP_200_OK)
    # except:
    #     response = {
    #         'status_code': status.HTTP_400_BAD_REQUEST,
    #         'message': 'Fields Missing',
    #     }
    #     return Response(response, status=status.HTTP_404_NOT_FOUND)


class AccountRegister(ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {
                'status_code': status.HTTP_200_OK,
                'account_id': serializer.data['account']['account_id'],
                'token': serializer.data['account']['token'],
            }
            return Response(response, status=status.HTTP_200_OK)
        except:
            response = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': 'Fields Missing',
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        account = Account_Module.objects.all().filter(account_id=request.data['account_id'])
        serializer=MiniAccountSerializer(instance=account,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DestinationRegister(RetrieveUpdateDestroyAPIView):
    serializer_class = DestinationSerializer
    permission_classes = (AllowAny, IsAuthenticated)
    authentication_classes = [JWTTokenUserAuthentication, ]

    def post(self, request, *args, **kwargs):
        module = Account_Module.objects.get(account_id=request.data['account_id'])
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(account=module)
        response = {
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully register',
        }
        return Response(response, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        account = Destination_Module.objects.all().filter(app_id=request.data['app_id'])
        serializer = MiniDestinationSerializer(instance=account,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            module = Destination_Module.objects.get(app_id=request.data['app_id'])
            if module is not None:
                serializer=DestinationSerializer(instance=module,data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                response = {
                    'status_code': status.HTTP_200_OK,
                    'message': 'Update Success',
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': 'App id not valid',
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'Message': 'App_ID not valid',
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User,username=request.data['username'])
        CheckPassword = check_password(request.data['password'], user.password)
        if CheckPassword:
            account = Account_Module.objects.all().filter(user=user)
            for i in account:
                print(i.account_id)
                Destination_Module.objects.filter(account=i).delete()
                i.delete()
                user.delete()
            response = {
                'status_code': status.HTTP_200_OK,
                'message': "All Related Data's Deleted",
                }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': "password does n't match",
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
