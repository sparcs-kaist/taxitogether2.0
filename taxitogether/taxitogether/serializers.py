from rest_framework import serializers

from taxitogether.models import Duck, Device


class DuckPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duck
        fields = ('username', 'gender', 'setting', 'date_joined')
        read_only_fields = ('setting', )
        depth = 1


class DuckRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duck
        fields = ('username', 'email', 'password', 'gender')


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'phone', 'token', 'device_type')
