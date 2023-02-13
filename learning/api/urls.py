

from django.urls import path,include
from api.views import *

# viewsets
from api import views
from rest_framework.routers import DefaultRouter
# creating router object 
router = DefaultRouter()
# register viewset with router 

# router.register('',views.Restframework,basename='database'),

# router.register('',views.API,basename='database'),

router.register('',views.ReadonlyAPI,basename='database'),




urlpatterns = [
    # function based crude 

    # path('',showall , name='showall'),


    # class based crude 

    # path('',DatabaseAPI.as_view()),


    # function based with ApiView

    # path('home/',reciverform ),
    # path('home/<int:pk>',reciverform),


    # class based with APIView

    # path('home/',Showall.as_view()),
    # path('home/<int:pk>',Showall.as_view()),


    # generic api view 

    # path('home/',nopk.as_view()),
    # path('home/<int:pk>',pk.as_view())


    # concrete api view 

    # path('home/',Addcreate.as_view()),
    # path('home/<int:pk>',Retrieveupdatedestory.as_view()),
    # path('home/<int:pk>',Retrievedestroy.as_view()),
    # path('home/<int:pk>',Retrieveupdate.as_view()),


    # viewsets

    # path('home/',include(router.urls)),

    # model viewsets

    path('home/',include(router.urls)),


]
