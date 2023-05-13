from django.urls import path
from . import views


urlpatterns = [
    path('', views.employ, name='employ'),
    path("getemployee/<int:deviceid>",views.employdetail,name='employdetail'),
    path("newemployee/<int:id>",views.newemployee,name='newemployee'),
    path("attandance/<int:id>",views.attandance,name='attandance'),
    path("delete_dub/<int:id>",views.delete_dub,name='delete_dub'),
    path("fresh/<str:ip>/<int:port>",views.fresh,name='fresh'),


]