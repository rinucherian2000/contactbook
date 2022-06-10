from django.urls import path
from book import views

urlpatterns = [
    path("phone/add", views.AddPhone.as_view(), name="phonecreate"),
    path("phone/all",views.PhoneList.as_view(),name="listphone"),
    path("books/details/<int:id>", views.PhoneDetail.as_view(), name="phonedetail"),
    path("books/edit/<int:id>",views.Phonedit.as_view(),name="phonedit"),
    path("books/delete/<int:id>", views.Phonedelete.as_view(), name="phonedelete"),

]