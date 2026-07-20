"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    views.py
"""

from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import (
    CanUploadEvidence,
    CanViewEvidence,
)
from .serializers import (
    EvidenceDetailSerializer,
    EvidenceListSerializer,
    EvidenceUploadSerializer,
)
from .services import EvidenceService


class EvidenceListView(ListAPIView):
    """
    List all evidence.
    """

    serializer_class = EvidenceListSerializer

    permission_classes = [
        IsAuthenticated,
        CanViewEvidence,
    ]

    def get_queryset(self):
        return EvidenceService.list_evidence()


class EvidenceDetailView(RetrieveAPIView):
    """
    Retrieve a single evidence item.
    """

    serializer_class = EvidenceDetailSerializer

    permission_classes = [
        IsAuthenticated,
        CanViewEvidence,
    ]

    lookup_field = "pk"

    def get_queryset(self):
        return EvidenceService.list_evidence()


class EvidenceUploadView(APIView):
    """
    Upload new evidence.
    """

    permission_classes = [
        IsAuthenticated,
        CanUploadEvidence,
    ]

    def post(self, request):

        serializer = EvidenceUploadSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        evidence = EvidenceService.upload_evidence(

            case=serializer.validated_data["case"],

            uploaded_file=serializer.validated_data["file"],

            uploaded_by=request.user,

            title=serializer.validated_data["title"],

            description=serializer.validated_data.get(
                "description",
                "",
            ),

            evidence_type=serializer.validated_data[
                "evidence_type"
            ],

            notes=serializer.validated_data.get(
                "notes",
                "",
            ),

            request=request,
        )

        return Response(

            EvidenceDetailSerializer(
                evidence
            ).data,

            status=status.HTTP_201_CREATED,
        )