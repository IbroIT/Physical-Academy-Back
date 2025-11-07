from rest_framework import viewsets
from rest_framework.response import Response
from .models import (
    IPChainInfo,
    IPChainStatistic,
    Patent,
    BlockchainFeature,
    IPChainBenefit,
    BlockchainData,
)
from .serializers import (
    IPChainInfoSerializer,
    IPChainStatisticSerializer,
    PatentSerializer,
    BlockchainFeatureSerializer,
    IPChainBenefitSerializer,
    BlockchainDataSerializer,
)


class IPChainInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для информации об IPChain.

    Поддерживает параметр ?lang=ru/en/kg для переводов.
    """

    queryset = IPChainInfo.objects.filter(is_active=True).prefetch_related(
        "translations"
    )
    serializer_class = IPChainInfoSerializer

    def list(self, request, *args, **kwargs):
        language = request.GET.get("lang", "ru")
        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset, many=True, context={"language": language}
        )
        return Response({"results": serializer.data})


class IPChainStatisticViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для статистики IPChain.

    Поддерживает параметр ?lang=ru/en/kg для переводов.
    """

    queryset = IPChainStatistic.objects.filter(is_active=True).prefetch_related(
        "translations"
    )
    serializer_class = IPChainStatisticSerializer

    def list(self, request, *args, **kwargs):
        language = request.GET.get("lang", "ru")
        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset, many=True, context={"language": language}
        )
        return Response({"results": serializer.data})


class PatentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для патентов в системе IPChain.

    Поддерживает параметр ?lang=ru/en/kg для переводов.
    """

    queryset = Patent.objects.filter(is_active=True).prefetch_related("translations")
    serializer_class = PatentSerializer

    def list(self, request, *args, **kwargs):
        language = request.GET.get("lang", "ru")
        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset, many=True, context={"language": language}
        )
        return Response({"results": serializer.data})


class BlockchainFeatureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для функций блокчейна IPChain.

    Поддерживает параметр ?lang=ru/en/kg для переводов.
    """

    queryset = BlockchainFeature.objects.filter(is_active=True).prefetch_related(
        "translations"
    )
    serializer_class = BlockchainFeatureSerializer

    def list(self, request, *args, **kwargs):
        language = request.GET.get("lang", "ru")
        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset, many=True, context={"language": language}
        )
        return Response({"results": serializer.data})


class IPChainBenefitViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для преимуществ IPChain.

    Поддерживает параметр ?lang=ru/en/kg для переводов.
    """

    queryset = IPChainBenefit.objects.filter(is_active=True).prefetch_related(
        "translations"
    )
    serializer_class = IPChainBenefitSerializer

    def list(self, request, *args, **kwargs):
        language = request.GET.get("lang", "ru")
        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset, many=True, context={"language": language}
        )
        return Response({"results": serializer.data})


class BlockchainDataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для данных блокчейна в реальном времени.

    Поддерживает параметр ?lang=ru/en/kg для переводов.

    Возвращает текущие данные блокчейна:
    - Текущий блок
    - Регистраций IP
    - Смарт-контрактов
    - Хэш сети
    """

    queryset = BlockchainData.objects.filter(is_active=True).prefetch_related(
        "translations"
    )
    serializer_class = BlockchainDataSerializer

    def list(self, request, *args, **kwargs):
        language = request.GET.get("lang", "ru")
        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset, many=True, context={"language": language}
        )
        return Response({"results": serializer.data})
