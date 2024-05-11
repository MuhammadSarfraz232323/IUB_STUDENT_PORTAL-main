from rest_framework import serializers 
from myapp.models import (
    Signup
    )
class Signup_serializer(serializers.ModelSerializer):
    model=Signup
    fields=[
        'name','father_name','phone_number','email_address','password','cnic'
    ]