from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from contents.models import Request, RequestMessage
from contents.serializers import RequestSerializer, RequestListSerializer, RequestMessageSerializer, AddRequestMessageSerializer


class CreateRequestAPIView(CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListRequestAPIView(ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestListSerializer
    permission_classes = [IsAuthenticated]


class RetrieveRequestAPIView(RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]
    

class CreateRequestMessageAPIView(CreateAPIView):
    queryset = RequestMessage.objects.all()
    serializer_class = AddRequestMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListRequestMessageAPIView(ListAPIView):
    serializer_class = RequestMessageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        qs = RequestMessage.objects.filter(request__id=pk)
        return RequestMessage.objects.filter(request__id=pk)
