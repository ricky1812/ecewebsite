from django.urls import path
from . import views

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from website import settings

urlpatterns=[
				path('',views.index,name='index'),
				path('signup/',views.signup,name='signup'),
				path('login/',views.login_view,name='login'),
				path('logout/',views.logout_view,name='logout'),
				path('update/',views.update_profile,name='update'),
				path('members/',views.member_list,name='members'),
			]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)