from rest_framework import serializers
from .models import Database


class DatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = '__all__'


    '''field level validation'''
    def validate_contactnumber(self,value):
        if value>9999999999 or value<9111111111:
            
            raise serializers.ValidationError('number cannot be more than or less than 10 digit')
        return value


    '''object level validation( multiple valiadate at once )'''
    def validate(self,value):
        gender = value.get('Gender')
        incident = value.get('incident')
        if gender=="M" and incident=="pregnant":
            raise serializers.ValidationError('please choose correct gender or indicent ')
        return value

    
    # def valdate_contactnumber(self,value):
    #     if Database.objects.filter(contactnumber = value):
    #         raise serializers.ValidationError('this contact number already exist ')
    #     return value

    # def validate_age(self,value):
    #     if value>18 or value<60:
    #         raise serializers.ValidationError('donor age cannot be more than 60 and less than 18')
    #     return value



        '''if we are using serializer like above way then we dont have to write down way other wise we have write 

            def create(self, validated_data):
                return super().create(validated_data)
            
            def update(self, instance, validated_data):
                return super().update(instance, validated_data)

        '''

