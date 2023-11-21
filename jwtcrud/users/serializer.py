from rest_framework import serializers
from .models import UserAccount, students
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['username','email','password']
        
    def validate(self, data):
        user = UserAccount(**data)
        password = data.get('password')
        try:
            validate_password(password, user)
        except exceptions.ValidationError as e:
            serializer_errors = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {'password': serializer_errors['non_field_errors']}
            )
        return data
    
    def create(self,validated_data):
        return UserAccount.objects.create_user(**validated_data)
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id','username','first_name','last_name','email',
                  'last_login','is_admin','is_staff','is_active','is_superuser']
        
class StudentSerializer(serializers.ModelSerializer):
    uploaded_by = UserSerializer(read_only=True)

    class Meta:
        model = students
        fields = ('id', 'name', 'uploaded_by', 'img', 'age', 'country')