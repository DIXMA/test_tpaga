from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.serializers import UserSerializer, AccountSerializer
from app.models import Account


class Accounts(APIView):

    def get(self, request):
        """
        Get all registered accounts
        :param request: Reques
        :return: Serializer data accounts
        @author: Diego Cortés <ingdiego.corts65@gmial.com>
        """
        accounts = Account.objects.all()
        accounts_serializer = AccountSerializer(accounts, many=True)
        return Response(accounts_serializer.data,
                        status=status.HTTP_201_CREATED)

    def post(self, request):
        """
        Register a new account
        :param request: Request data for new account
        :return: Serializer account data register
        @author: Diego Cortés <ingdiego.corts65@gmial.com>
        """
        try:
            serializer = AccountSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Internal server error",
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AccountsUpdate(APIView):

    def put(self, request, pk):
        """
        Update balance for an account
        :param request: Request
        :param pk: Pk for search account to update
        :return: Serialiser acciun data updated
        @author: Diego Cortés <ingdiego.corts65@gmial.com>
        """
        try:
            account = Account.objects.get(pk=pk)
            if account:
                serializer = AccountSerializer(account, many=False)
                if request.POST['balance']:
                    account.balance += float(request.POST['balance'])
                    account.save()
                    return Response(serializer.data,
                                    status=status.HTTP_201_CREATED)
                return Response("Balance data not found",
                                status=status.HTTP_404_NOT_FOUND)
            return Response("Account not found",
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Internal server error",
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
