from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken

from pusher.models import Account_Module, Destination_Module


class AccountSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=False)
    token = serializers.CharField(required=False)

    class Meta:
        model = Account_Module
        fields = ('user', 'account_id', 'account_name', 'website', 'token')

    def create(self, validated_data):
        user_data = User.objects.get(username=validated_data['user'])
        jwt_token = AccessToken.for_user(user_data)
        try:
            if validated_data['website']:
                website = validated_data['website']
            else:
                website = ''
        except Exception as e:
            error = e
            website = ''
        account_data = Account_Module.objects.create(
            user=user_data,
            account_id=validated_data['account_id'],
            account_name=validated_data['account_name'],
            website=website,
            token=jwt_token
        )
        account_data.save()
        rec = dict()
        rec['token'] = jwt_token
        rec['account_name'] = account_data.account_name
        return account_data


class MiniAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account_Module
        fields = ('account_id', 'token')


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'account')
        extra_kwargs = {'password': {'write_only': True}, 'account': {'write_only': True},
                        'username': {'write_only': True}}

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        password = validated_data['password']
        user_data = User.objects.create_user(
            email=email,
            username=username,
            password=password
        )
        jwt_token = AccessToken.for_user(user_data)
        profile = validated_data.pop('account')
        try:
            if profile['website']:
                website = profile['website']
            else:
                website = ''
        except Exception as e:
            error = e
            website = ''
        account_data = Account_Module.objects.create(
            user=user_data,
            account_id=profile['account_id'],
            account_name=profile['account_name'],
            website=website,
            token=jwt_token
        )
        return {"account": account_data, "username": user_data}


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination_Module
        fields = ('app_id', 'app_name', 'app_software', 'app_secret')

    def create(self, validated_data):
        destination = Destination_Module.objects.create(**validated_data)
        return destination

    def update(self, instance, validated_data):
        instance.app_name = validated_data.get('app_name', instance.app_name)
        instance.app_software = validated_data.get('app_software', instance.app_software)
        instance.app_secret = validated_data.get('app_secret', instance.app_secret)
        instance.save()
        return instance


class MiniDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination_Module
        fields = ('account','app_id', 'app_name', 'app_software', 'app_secret','create_date','update_date')
