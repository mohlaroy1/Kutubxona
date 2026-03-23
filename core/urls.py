from django.contrib import admin
from django.urls import path
from main_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salom_view),
    path('', home_view),
    path('talabalar/', talabalar_view),
    path('talabalar/<int:talaba_id>/', talaba_view),
    path('talaba_add/', talaba_add_view),
    path('talabalar/<int:pk>/delete/', talaba_delete_view),
    path('talabalar/<int:pk>/update/', talaba_update_view),
    path('talabalar/<int:pk>/delete_confirm/', talaba_delete_confirm_view),
    path('kitoblar/', kitoblar_view),
    path('kitoblar/<int:kitob_id>/', kitob_view),
    path('kitob_add/', kitob_add_view),
    path('kitoblar/<int:pk>/update/', kitob_update_view),
    path('kitoblar/<int:pk>/delete/', kitob_delete_view),
    path('kitoblar/<int:pk>/delete_confirm/', kitob_delete_confirm_view),
    path('mualliflar/', mualliflar_view),
    path('mualliflar/<int:muallif_id>/', muallif_view),
    path('muallif_add/', muallif_add_view),
    path('mualliflar/<int:pk>/update/', muallif_update_view),
    path('kutubxonachilar/', kutubxonachilar_view),
    path('kutubxonachilar/<int:kutubxonachi_id>/', kutubxonachi_view),
    path('kutubxonachi_add/', kutubxonachi_add_view),
    path('kutubxonachilar/<int:pk>/update/', kutubxonachi_update_view),
    path('recordlar/', recordlar_view),
    path('recordlar/<int:record_id>/', record_view),
    path('record_add/', record_add_view),
    path('recordlar/<int:pk>/update/', record_update_view),

]
