"""
Digital Evidence Management System (DEMS)

Module:
    Cases

File:
    views.py

Purpose:
    REST API views for Case Management.
"""
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from .filters import CaseFilter
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Case
from .permissions import (
    CanArchiveCase,
    CanAssignCase,
    CanCloseCase,
    CanCreateCase,
    CanDeleteCase,
    CanUpdateCase,
    CanViewCase,
)
from .serializers import (
    CaseCreateSerializer,
    CaseDetailSerializer,
    CaseListSerializer,
    CaseUpdateSerializer,
)
from .services import CaseService


class CaseListView(ListAPIView):

    queryset = (
        Case.objects
        .select_related(
            "case_type",
            "status",
            "priority",
            "department",
            "lead_investigator",
            "created_by",
        )
        .order_by("-created_at")
    )

    serializer_class = CaseListSerializer

    permission_classes = [CanViewCase]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = CaseFilter

    search_fields = [
        "case_number",
        "title",
        "description",
        "court_reference",
    ]

    ordering_fields = [
        "case_number",
        "title",
        "date_opened",
        "created_at",
    ]

    ordering = [
        "-created_at",
    ]

class CaseDetailView(RetrieveAPIView):
    """
    Retrieve a single case.
    """

    queryset = (
        Case.objects
        .select_related(
            "case_type",
            "status",
            "priority",
            "department",
            "lead_investigator",
            "created_by",
        )
        .prefetch_related(
            "assignments",
            "notes",
            "attachments",
        )
    )

    serializer_class = CaseDetailSerializer
    permission_classes = [CanViewCase]


class CaseCreateView(CreateAPIView):
    """
    Create a new case.
    """

    serializer_class = CaseCreateSerializer
    permission_classes = [CanCreateCase]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        case = CaseService.create_case(
            serializer.validated_data,
            request.user,
        )

        return Response(
            {
                "success": True,
                "message": "Case created successfully.",
                "data": CaseDetailSerializer(case).data,
            },
            status=status.HTTP_201_CREATED,
        )


class CaseUpdateView(UpdateAPIView):
    """
    Update an existing case.
    """

    queryset = Case.objects.all()

    serializer_class = CaseUpdateSerializer

    permission_classes = [CanUpdateCase]

    def update(self, request, *args, **kwargs):

        case = self.get_object()

        serializer = self.get_serializer(
            case,
            data=request.data,
            partial=True,
        )

        serializer.is_valid(raise_exception=True)

        updated_case = CaseService.update_case(
            case,
            serializer.validated_data,
        )

        return Response(
            {
                "success": True,
                "message": "Case updated successfully.",
                "data": CaseDetailSerializer(updated_case).data,
            }
        )


@extend_schema(
    responses={204: None},
)
class CaseDeleteView(DestroyAPIView):
    """
    Delete a case.
    """

    queryset = Case.objects.all()

    serializer_class = CaseDetailSerializer

    permission_classes = [CanDeleteCase]

    def destroy(self, request, *args, **kwargs):

        case = self.get_object()

        CaseService.delete(case)

        return Response(
            {
                "success": True,
                "message": "Case deleted successfully.",
            },
            status=status.HTTP_204_NO_CONTENT,
        )


@extend_schema(
    responses={200: CaseDetailSerializer},
)
class CloseCaseView(APIView):
    """
    Close a case.
    """

    serializer_class = CaseDetailSerializer
    
    permission_classes = [CanCloseCase]

    def post(self, request, pk):

        case = CaseService.get_object(Case, pk=pk)

        case = CaseService.close_case(case)

        return Response(
            {
                "success": True,
                "message": "Case closed successfully.",
                "data": CaseDetailSerializer(case).data,
            }
        )


@extend_schema(
    responses={200: CaseDetailSerializer},
)
class ReopenCaseView(APIView):
    """
    Reopen a case.
    """

    serializer_class = CaseDetailSerializer
    
    permission_classes = [CanCloseCase]

    def post(self, request, pk):

        case = CaseService.get_object(Case, pk=pk)

        case = CaseService.reopen_case(case)

        return Response(
            {
                "success": True,
                "message": "Case reopened successfully.",
                "data": CaseDetailSerializer(case).data,
            }
        )


@extend_schema(
    responses={200: CaseDetailSerializer},
)
class ArchiveCaseView(APIView):
    """
    Archive a case.
    """

    serializer_class = CaseDetailSerializer
    
    permission_classes = [CanArchiveCase]

    def post(self, request, pk):

        case = CaseService.get_object(Case, pk=pk)

        case = CaseService.archive_case(case)

        return Response(
            {
                "success": True,
                "message": "Case archived successfully.",
                "data": CaseDetailSerializer(case).data,
            }
        )