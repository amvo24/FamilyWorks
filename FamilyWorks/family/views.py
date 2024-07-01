from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Family, FamilyMembership, Invitation
from .serializers import FamilySerializer, FamilyMembershipSerializer, InvitationSerializer
from user.serializers import UserSerializer

# Create your views here.
class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Family.objects.filter(members__user=user)

    @action(detail=True, methods=['get'])
    def list_members(self, request, **kwargs):
        family = self.get_object()
        memberships = FamilyMembership.objects.filter(family=family)
        members = [membership.user for membership in memberships]
        serializer = UserSerializer(members, many=True)
        return Response(serializer.data)


class FamilyMembershipViewSet(viewsets.ModelViewSet):
    queryset = FamilyMembership.objects.all()
    serializer_class = FamilyMembershipSerializer
    permission_classes = [permissions.IsAuthenticated]


class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Invitation.objects.filter(accepted=None)

    @action(detail=False, methods=['get'], url_path='sent-invitations')
    def sent_invitations(self, request):
        user = request.user
        sent_invitations = Invitation.objects.filter(invited_by=user, accepted=None)
        serializer = self.get_serializer(sent_invitations, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='received-invitations')
    def received_invitations(self, request):
        user = request.user
        received_invitations = Invitation.objects.filter(recipient_email=user.email, accepted=None)
        serializer = self.get_serializer(received_invitations, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def accept(self, request, **kwargs):
        invitation = self.get_object()

        FamilyMembership.objects.create(user=request.user, family=invitation.family)
        invitation.accepted = True
        invitation.save()

        return Response({'status': 'Invitation accepted'}, status=status.HTTP_200_OK)


    @action(detail=True, methods=['post'])
    def decline(self, request, **kwargs):
        invitation = self.get_object()

        if invitation.recipient != request.user:
            return Response({"detail": "You are not allowed to decline this invitation."}, status=status.HTTP_403_FORBIDDEN)
        invitation.accepted = False
        invitation.save()
        return Response({"detail": "Invitation declined."}, status=status.HTTP_200_)
