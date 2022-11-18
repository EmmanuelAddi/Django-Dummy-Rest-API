from rest_framework import viewsets
from rest_framework.response import Response
from snippets.models  import Snippet
from .serializers import SnippetSerializer

class SnippetViewSet(viewsets.ViewSet):
    
    def list (self, request):
        queryset = Snippet.objects.all()
        serializer = SnippetSerializer(queryset, many=True)
        return Response(serializer.data)
        

#class SnippetViewSet(viewsets.ModelViewSet):
#    queryset = Snippet.objects.all()
#    serializer_class = SnippetSerializer

