from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('arts/', views.arts_index, name='index'),
    path('arts/<int:art_id>/', views.arts_detail, name='detail'),
    path('arts/create/', views.ArtCreate.as_view(), name='arts_create'),
    path('arts/<int:pk>/update/', views.ArtUpdate.as_view(), name='arts_update'),
    path('arts/<int:pk>/delete/', views.ArtDelete.as_view(), name='arts_delete'),
    path('arts/<int:art_id>/add_exhibition/', views.add_exhibition, name='add_exhibition'),
    path('buyers/', views.BuyerList.as_view(), name='buyers_index'),
    path('buyers/<int:pk>/', views.BuyerDetail.as_view(), name='buyers_detail'),
    path('buyers/create/', views.BuyerCreate.as_view(), name='buyers_create'),
    path('buyers/<int:pk>/update/', views.BuyerUpdate.as_view(), name='buyers_update'),
    path('buyers/<int:pk>/delete/', views.BuyerDelete.as_view(), name='buyers_delete'),
    # associate a buyer with an art
    path('arts/<int:art_id>/assoc_buyer/<int:buyer_id>/', views.assoc_buyer, name='assoc_buyer'),
]