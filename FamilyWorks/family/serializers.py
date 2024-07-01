from rest_framework import serializers
from .models import Family, FamilyMembership, Invitation
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer

User = get_user_model()

class FamilySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.full_name')
    # members = serializers.ReadOnlyField(source='members.user.full_name')
    members = serializers.SerializerMethodField()

    class Meta:
        model = Family
        fields = [
            "id",
            "name",
            "description",
            "created_by",
            "members"
        ]
        read_only_fields = ['created_by']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        family = Family.objects.create(**validated_data)  # Create the Family instance
        FamilyMembership.objects.create(user=user, family=family)
        return family

    def get_members(self, obj):
        family_memberships = FamilyMembership.objects.filter(family=obj)
        users = [membership.user for membership in family_memberships]
        return UserSerializer(users, many=True).data




class FamilyMembershipSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.full_name')
    class Meta:
        model = FamilyMembership
        fields = [
            "id",
            "family",
            "user",
            "joined_at"
        ]
        read_only_fields = ['joined_at']


class InvitationSerializer(serializers.ModelSerializer):
    invited_by = serializers.ReadOnlyField(source='invited_by.full_name')
    recipient = serializers.ReadOnlyField(source='recipient.full_name')

    class Meta:
        model = Invitation
        fields = [
            "id",
            "invitation_token",
            "family",
            "invited_by",
            "recipient",
            "recipient_email",
            "expiry_date",
            "accepted"
        ]
        read_only_fields = [
            "invitation_token",
            "invited_by",
            "expiry_date",
            "accepted"
        ]

    def create(self, validated_data):
        sender = self.context['request'].user
        validated_data['invited_by'] = sender
        recipient_email = validated_data.get('recipient_email')
        recipient = User.objects.get(email=recipient_email)
        validated_data['recipient'] = recipient
        invitation = super().create(validated_data)
        return invitation
