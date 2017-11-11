from django.conf.urls import *

from user.views import home


urlpatterns = [
				url(r"^home/$", home, name='user_home' ),
			]