from django.contrib import admin
from django.urls import path, include
from predictor import views as predictor_views  # ✅ Import views from predictor app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', predictor_views.home, name='home'),         # Homepage
    path('predict/', predictor_views.predict, name='predict'),  # Prediction logic
    path('result/', predictor_views.result, name='result'),     # Result display

    path('users/', include('users.urls')),  # ✅ Routes for login, signup, etc.
]
