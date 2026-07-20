"""
Digital Evidence Management System (DEMS)

Module:
    Chain of Custody

File:
    views.py
"""

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.evidence.models import Evidence

from .filters import CustodyFilter
from .models import CustodyRecord
from .permissions import (
    CanTransferEvidence,
    CanViewCustody,
)
from .serializers import (
    CustodyDetailSerializer,
    CustodyListSerializer,
    CustodyTransferSerializer,
)
from .services import CustodyService


class CustodyListView(ListAPIView):
    """
    List all custody records.
    """

    queryset = (
        CustodyRecord.objects
        .select_related(
            "evidence",
            "from_user",
            "to_user",
        )
        .order_by("-transferred_at")
    )

    serializer_class = CustodyListSerializer

    permission_classes = [CanViewCustody]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = CustodyFilter

    search_fields = [
        "evidence__evidence_number",
        "location",
        "reason",
    ]

    ordering_fields = [
        "transferred_at",
    ]


class CustodyDetailView(RetrieveAPIView):

    queryset = CustodyRecord.objects.select_related(
        "evidence",
        "from_user",
        "to_user",
    )

    serializer_class = CustodyDetailSerializer

    permission_classes = [CanViewCustody]


class CustodyTransferView(APIView):

    permission_classes = [CanTransferEvidence]

    def post(self, request):

        serializer = CustodyTransferSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        evidence = get_object_or_404(
            Evidence,
            pk=serializer.validated_data["evidence"].pk,
        )

        custody = CustodyService.transfer_evidence(
            evidence=evidence,
            from_user=request.user,
            to_user=serializer.validated_data["to_user"],
            action=serializer.validated_data["action"],
            location=serializer.validated_data["location"],
            reason=serializer.validated_data["reason"],
            remarks=serializer.validated_data.get(
                "remarks",
                "",
            ),
            request=request,
        )

        return Response(
            CustodyDetailSerializer(custody).data,
            status=status.HTTP_201_CREATED,
        )