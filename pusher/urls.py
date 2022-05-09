from django.conf.urls.static import static
from django.urls import path

from data import settings
from pusher.views import DestinationRegister, AccountRegister, Accounts

urlpatterns = [
    path('account/incoming_data', AccountRegister.as_view()),
    path('account/', Accounts.as_view()),
    path('server/incoming_data', DestinationRegister.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
