from django.urls import path
from pet import views

urlpatterns = [
    path('add/', views.pet_and_measure_form, name='pet_add'),
    path('pet_edit/<int:pk>/', views.pet_and_measure_form,
         name='pet_edit'),
    path('pet_delete/<int:pk>/', views.PetDeleteView.as_view(),
         name='pet_delete'),
    path('add_pet_measure/', views.PetMeasureView.as_view(),
         name='add_pet_measure'),
    path('add_pet_medcard/', views.PetMedCardView.as_view(),
         name='add_pet_medcard'),
    path('pet_medcard/<int:pk>/', views.med_card_view,
         name='pet_medcard'),
    path('pet_measure/<int:pk>/', views.measure_view,
         name='pet_measure'),
    path('', views.type_search, name='search'),
]
