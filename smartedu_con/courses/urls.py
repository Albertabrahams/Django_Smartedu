from django.urls import path
from .views import course_detail, course_list, category_list, tag_list

urlpatterns = [
    path('', course_list, name = "courses"),
    path('<slug:category_slug>/<int:course_id>', course_detail, name = "course_detail"),
    path('categories/<slug:category_slug>', category_list, name = "courses_by_category"),
    path('tags/<slug:tag_slug>', tag_list, name = "courses_by_tag"),
    
] 