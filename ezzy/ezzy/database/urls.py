from django.urls import path,include
from . import views
urlpatterns = [

    path("",views.homepage,name = "homepage"),
    #path("test",views.graph,name = "homepage"),
    #path("graph",views.grp_rndr,name = "graph"),
    path("update",views.update,name = "graph"),
    path("save_cust",views.ajax_update,name = "save"),
    path('open',views.open,name = "opne"),
    path("jq_aj",views.jquery_ajax,name = "jq"),

]
