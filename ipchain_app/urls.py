from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    IPChainInfoViewSet,
    IPChainStatisticViewSet,
    PatentViewSet,
    BlockchainFeatureViewSet,
    IPChainBenefitViewSet,
    BlockchainDataViewSet,
)

router = DefaultRouter()
router.register(r"info", IPChainInfoViewSet, basename="ipchain-info")
router.register(r"stats", IPChainStatisticViewSet, basename="ipchain-stats")
router.register(r"patents", PatentViewSet, basename="ipchain-patents")
router.register(r"features", BlockchainFeatureViewSet, basename="ipchain-features")
router.register(r"benefits", IPChainBenefitViewSet, basename="ipchain-benefits")
router.register(
    r"blockchain-data", BlockchainDataViewSet, basename="ipchain-blockchain-data"
)

urlpatterns = [
    path("", include(router.urls)),
]
