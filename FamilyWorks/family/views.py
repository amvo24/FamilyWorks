from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Family, FamilyMembership
from .serializers import FamilySerializer
from user.serializers import UserSerializer

# Create your views here.
class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

    def get_queryset(self):
        user = self.request.user
        return Family.objects.filter(familymembership__user=user)

    @action(detail=True, methods=['get'])
    def list_members(self, request, **kwargs):
        family = self.get_object()
        memberships = FamilyMembership.objects.filter(family=family)
        members = [membership.user for membership in memberships]
        serializer = UserSerializer(members, many=True)
        return Response(serializer.data)
