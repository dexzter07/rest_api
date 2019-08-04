from rest_framework import serializers
from .models import employees,user_auth


class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        fields = ("first_name","last_name")


class signup(serializers.ModelSerializer):

    class Meta:
        model = user_auth
        fields = ("user_name","password","token")
