import uuid
from .models import Author, Article
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from .documents import AuthorDocument, ArticleDocument
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from .serializers import AuthorDocumentSerializer, ArticleDocumentSerializer
from .serializers import AuthorSerializer, ArticleSerializer, ArticleAnonSerializer, RegisterSerializer


class IsAdminOrReadOnly(BasePermission):
    message = 'You need admin status to complete this operation'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff


class AuthorsViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return ArticleSerializer
        else:
            return ArticleAnonSerializer


class Register(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",

                "User": serializer.data}, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorSearchWithESViewSet(DocumentViewSet):
    document = AuthorDocument
    serializer_class = AuthorDocumentSerializer

    filter_backends = [SearchFilterBackend]

    search_fields = {
        "id",
        "name",
        "picture",
    }

    filter_fields = {
        "id": "id",
        "name": "name",
        "picture": "picture",
    }


class ArticleSearchWithESViewSet(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleDocumentSerializer

    filter_backends = [SearchFilterBackend]

    search_fields = {
        "id",
        "category",
        "title",
        "summary",
        "first_paragraph",
        "body",
    }

    filter_fields = {
        "id": "id",
        "category": "category",
        "title": "title",
        "summary": "summary",
        "first_paragraph": "first_paragraph",
        "body": "body",
    }