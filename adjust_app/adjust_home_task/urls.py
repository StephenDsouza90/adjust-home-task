from django.urls import path
from .views import Views


urlpatterns = [
    path('', Views().home, name='home'),
    path('add-data', Views().add_performace_metrics_data, name='add_data'),
    path('get-data', Views().get_performace_metrics_data, name='get_data'),
]
