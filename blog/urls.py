from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'blog'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^essay/$', views.essay, name='essay'),
	url(r'^worklog/$', views.worklog, name='worklog'),
	url(r'^joke/$', views.joke, name='joke'),
	url(r'^others/$', views.others, name='others'),
	url(r'^blog_detail/blog_(?P<blog_id>\d+)/$', views.blog_detail, name='blog_detail'),
	url(r'^tags/tag_(?P<blog_id>\d+)/$', views.tag, name='tag'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)