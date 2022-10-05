from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


class BaseListRetrieveViewSet(
    ListModelMixin, RetrieveModelMixin, GenericViewSet
):
    pass
