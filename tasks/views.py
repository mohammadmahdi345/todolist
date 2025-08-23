from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task, Timeslot
from .serializers import TaskSerializer, TimeSerializer

class TaskView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskButtonView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            task = Task.objects.get(user=request.user, completed=False, pk=pk)
        except Task.DoesNotExist:
            return Response(status=404)

        task.completed = True
        task.save()
        return Response({'detail': 'تسک انجام شد'}, status=200)


class TaskStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_tasks = Task.objects.filter(user=request.user).count()
        completed_tasks = Task.objects.filter(user=request.user, completed=True).count()
        incomplete_tasks = total_tasks - completed_tasks
        return Response({
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'incomplete_tasks': incomplete_tasks
        })






class TimeslotView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            task = Task.objects.get(user=request.user, pk=pk)
        except Task.DoesNotExist:
            return Response(status=404)
        serializer = TimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(task=task)
            return Response('تایم ثبت شد', status=201)
        return Response(serializer.errors, status=400)

class TimeslotGetView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        time = Timeslot.objects.filter(task__user=request.user)
        if not time.exists():
            return Response(status=404)
        serializer = TimeSerializer(time, many=True)
        return Response(serializer.data, status=200)


