from rest_framework import viewsets, mixins, permissions

from taxitogether.models import Duck, Device
from taxitogether import serializers


class DuckViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    model = Duck

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.DuckRegisterSerializer
        elif self.request.method == 'GET':
            return serializers.DuckPublicSerializer
        else:
            raise Exception("Not allowed method %s" % str(self.request.method))


class DeviceViewSet(viewsets.ModelViewSet):
    model = Device
    serializer_class = serializers.DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def pre_save(self, obj):
        # Set device owner to the requested user
        obj.owner = self.request.user

    def get_queryset(self):
        # Filter only the device of requested user
        return self.request.user.devices.all()
