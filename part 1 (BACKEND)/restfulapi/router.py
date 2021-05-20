from myapi.viewsets import BranchesViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Branches',BranchesViewset)