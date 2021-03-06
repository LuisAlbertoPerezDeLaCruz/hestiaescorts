from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^404.html$', views.v404, name='v404'),
    url(r'^about.html$', views.about, name='about'),
    url(r'^blog-home-1.html$', views.blog_home_1, name='blog-home-1'),
    url(r'^blog-home-2.html$', views.blog_home_2, name='blog-home-2'),
    url(r'^blog-post.html$', views.blog_post, name='blog-post'),
    url(r'^contact.html$', views.contact, name='contact'),
    url(r'^faq.html$', views.faq, name='faq'),
    url(r'^portfolio-item.html$', views.portfolio_item, name='portfolio-item'),
    url(r'^pricing.html$', views.pricing, name='pricing'),
    url(r'^services.html$', views.services, name='services'),
    url(r'^sidebar.html$', views.sidebar, name='sidebar'),
    url(r'^provincia-(?P<pk>[\w\-]+).html$', views.portfolio_provincia, name='portfolio_provincia'),
    url(r'^ciudad', views.ciudad, name='ciudad'),
    url(r'^portfolio-(?P<pk>[\w\-]+)$', views.portfolio_escort, name='portfolio'),
    url(r'^escort-upload-images$', views.escort_upload_images, name='escort-upload-images'),
    url(r'^conf-escort-(?P<pk>[\w\-]+)$', views.conf_escort, name='conf-escort'),
    url(r'^escort-update-info$', views.escort_update_info, name='escort-update-info'),

]
