from django.urls import path, re_path
from . import views

urlpatterns = [

    # path('get-sysmodel/', views.ReturnSysModelStatus.as_view()),
    # path('get-sysdevicelatency/', views.ReturnSysDeviceLatency.as_view()),
    path('get-sysmodel/', views.ReturnSysDeviceLatency.as_view()),
    
    path('get-device/', views.ReturnDeviceStatus.as_view()),
    path('get-mission/', views.ReturnMissionStatus.as_view()),
    path('compress-model/', views.ReturnCompressModel.as_view()),
    re_path('^download-model/', views.DownloadCompressModel.as_view()),
    re_path('^download-sysmodel/', views.DownloadSysModel.as_view()),
    re_path('^download-sysmodelcode/', views.DownloadSysModelCode.as_view()),
    re_path('^download-modeldefinition/', views.DownloadModeldefinition.as_view()),
    # path('ip-connect/', views.ConnectReturnDevice.as_view())

]