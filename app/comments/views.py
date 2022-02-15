from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from comments.models import CommentChore
from comments.permissions import IsHouseMember
from comments.serializers import CommentChoreSerializer

class CommentChoreViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    queryset = CommentChore.objects.all()
    serializer_class = CommentChoreSerializer
    permission_classes = [IsAuthenticated, IsHouseMember]

    def list(self, request, chore_id, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(chore_id=chore_id)
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)