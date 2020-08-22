from django.urls import path
from . import views   # ho importato l'url di django e le nostre views dall'app blog

urlpatterns = [
    path('',views.post_list, name ='post_list'), # sto assegnando una view chiam
    #post list alla URL. Essendo campo vuoto django ignora il nome dominio .
    # Questo schema dirà a Django che views.post_list è il posto giusto
    # name = 'postl_list' è il nome dell'URL che verrà usata per identificare la view
]