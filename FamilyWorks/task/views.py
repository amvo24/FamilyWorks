from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Task
from family.models import FamilyMembership, Family
from .serializers import TaskSerializer
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import PermissionDenied, NotFound
from notifications.utils import create_notification


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        family_ids = FamilyMembership.objects.filter(user=user).values_list('family_id', flat=True)
        return Task.objects.filter(family_id__in=family_ids)

    def perform_create(self, serializer):
        task = serializer.save()
        return super().perform_create(serializer)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if instance == user or FamilyMembership.objects.filter(user=user, family=instance.family).exists():
            return super().retrieve(request, *args, **kwargs)

        return Response({"detail": "You do not have permission to view this task."}, status=status.HTTP_403_FORBIDDEN)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.created_by != request.user:
            return Response({"detail": "You do not have permission to update this task."}, status=status.HTTP_403_FORBIDDEN)

        content = f"Task '{instance.title}' has been updated."
        create_notification(instance.created_by.id, request.user.id, 'TASK', content, task=instance)
        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def get_assigned_tasks(self, request):
        user = self.request.user
        tasks = Task.objects.get(assigned_to=user)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)


    @action(detail=True, methods=['get'])
    def get_family_tasks(self, request, pk=None):
        try:
            family = Family.objects.get(pk=pk)
        except Family.DoesNotExist:
            raise Http404("Family not found")

        if not FamilyMembership.objects.filter(family=family, user=request.user).exists():
            raise PermissionDenied("You do not have permission to view tasks for this family.")

        tasks = Task.objects.filter(family=family)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
