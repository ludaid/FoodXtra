"""foodwaste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from app import views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.project),
    path('form/',views.forms),
    path('admin1/',views.admin1),
    path('adminheader/',views.adminheader),
    path('publicvolunteerregistration/',views.publicvolunteerregistration),
    path('publicinsertvolunteer/',views.publicinsertvolunteer),
    path('publicbeneficiarregistration/',views.publicbeneficiarregistration),
    path('publicinsertbeneficiar/',views.publicinsertbeneficiar),
    path('adminvolunteerregistration/',views.adminvolunteerregistration),
    path('admininsertvolunteer/',views.admininsertvolunteer),
    path('adminvolunteerviewremove/',views.adminvolunteerviewremove),
    path('removevolunteer/<str:name>',views.removevolunteer),
    path('adminvolunteerviewverification/',views.adminvolunteerviewverification),
    path('accept/<str:id1>',views.accept),
    path('reject/<str:id1>',views.reject),
    path('adminremovebeneficiar/',views.adminremovebeneficiar),
    path('removebeneficiar/<str:id1>',views.removebeneficiar),
    path('adminverifybeneficiar/',views.adminverifybeneficiar),
    path('accept_beneficiar/<str:bid>',views.accept_beneficiar),
    path('reject_beneficiar/<str:bid>',views.reject_beneficiar),
    path('login/',views.login),
    path('log/',views.log),
    path('volunteers/',views.volunteers),
    path('beneficiars/',views.beneficiars),
    path('fooddonation/',views.fooddonation),
    path('publicinsertdonation/',views.publicinsertdonation),
    path('beneficiarselectcatagory/',views.beneficiarselectcatagory),
    path('beneficiarviewavailability/',views.beneficiarviewavailability),
    path('beneficiargeneraterequest/<str:id1>',views.beneficiargeneraterequest),
    path('beneficiarinsertfoodrequest/',views.beneficiarinsertfoodrequest),#validation
    path('adminviewcomplaint/',views.adminviewcomplaint),
    path('adminpublicrequestprocess/',views.adminpublicrequestprocess),
    path('accept_request/<str:id1>',views.accept),
    path('reject_request/<str:id1>',views.reject),
    path('admindutyallotment/',views.admindutyallotment),
    path('accept_beneficiarrequest/<str:id1>',views.accept_beneficiarrequest),
    path('reject_beneficiarrequest/<str:id1>',views.reject_beneficiarrequest),
    path('adminallotfoodbeneficiars/',views.adminallotfoodbeneficiars),
    path('publicrequesttypeselect/',views.publicrequesttypeselect),
    path('viewfooddonation/',views.viewfooddonation),
    path('foodrequest/<str:id>',views.foodrequest),
    path('publicrequestupdation/<str:id>',views.publicrequestupdation),
    path('beneficiaryhome/',views.beneficiaryhome),
    path('beneficiaryfoodreq/',views.beneficiaryfoodreq),
    path('beneficiaryfoodreqcomplete/',views.beneficiaryfoodreqcomplete),
    path('benfoodrequest/<str:id>',views.benfoodrequest),
    path('benrequestupdation/<str:id>',views.benrequestupdation),
    path('beneficiarycompl/',views.beneficiarycompl),
    path('beneficiaryreview/',views.beneficiaryreview),
    path('beneficiarycomplupdate/',views.beneficiarycomplupdate),
    path('beneficiaryreviewupdate/',views.beneficiaryreviewupdate),
    path('adminpublicfoodrequest/',views.adminpublicfoodrequest),
    path('adminbeneficiaryfoodreq/',views.adminbeneficiaryfoodreq),
    path('acceptpublicfoodreq/<str:id2>',views.acceptpublicfoodreq),
    path('rejectpublicfoodreq/<str:id3>',views.rejectpublicfoodreq),
    path('acceptbeneficiaryfoodrequest/<str:id4>',views.acceptbeneficiaryfoodrequest),
    path('rejectbeneficiaryfoodrequest/<str:id5>',views.rejectbeneficiaryfoodrequest),
    path('beneficiaryfoodstatus/',views.beneficiaryfoodstatus),
    path('orderstatus/',views.orderstatus),
    path('orderstatuspublicdon/',views.orderstatuspublicdon),
    path('orderstatuspublicdontable/',views.orderstatuspublicdontable),
    path('donordonationstatus/',views.donordonationstatus),
    path('admindonation/',views.admindonation),
    path('accept_food/<str:id6>',views.accept_food),
    path('publicdonorregistration/',views.publicdonorregistration),
    path('publicinsertdonor/',views.publicinsertdonor),
    path('forget/',views.forget),
    path('forget1/',views.forget1),
    path('forget2/',views.forget2),
    path('forget3/',views.forget3),
    path('adminverifydonor/',views.adminverifydonor),

    path('accept_donor/<str:did>',views.accept_donor),
    path('reject_donor/<str:did>',views.reject_donor),
    
    path('adminremovedonor/',views.adminremovedonor),

    path('removedonor/<str:id1>',views.removedonor),
    #donor page
    path('donorhome/',views.donorhome),
    path('donordonation/',views.donordonation),
    path('donorinsertdonation/',views.donorinsertdonation),   
    path('editquantity/<str:id>',views.editquantity),  
    path('edit/<str:id>',views.edit),  
    path('donations/',views.donations),
    path('donorremovefood/<str:id2>',views.donorremovefood),
    path('publicpickup/',views.publicpickup),
    path('publicreview/',views.publicreview),
    path('publicreviewinsert/',views.publicreviewinsert),
    path('admincomplaint/',views.admincomplaint),
    path('donorcomplaint/',views.donorcomplaint),
    path('donorcompl/',views.donorcompl),
    path('donorcomplupdate/',views.donorcomplupdate),
    path('donorreview/',views.donorreview),
    path('donorreviewupdate/',views.donorreviewupdate),
    path('publicre/',views.publicre),
    path('donorre/',views.donorre),
    path('benre/',views.benre),
    path('indextesting/',views.indextesting),
    path('profile/',views.profile),
    # path('logout_request/',views.logout_request),
]
if settings.DEBUG:
        urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
