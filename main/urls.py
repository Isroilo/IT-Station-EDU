from django.urls import path
from .views import *
urlpatterns = [
    path("student/", student_view),
    path("teacher/", teacher_view),
    path("director/", director_view),
    path("reception/", reception_view),
    path("group/", group_view),
    path("get_student_by_group/<int:pk>/", get_student_by_group),
    path("filter_group_by_time/<int:pk>/", filter_group_by_time),
#     path("subcategory/", subcategory_view),
#     path("banner/", banner_view),
#     path("recomended_product/", recomended_product_view),
#     path("top_product/", top_product_view),
#     path("create_comment/<int:pk>/", create_comment),
#     path("reply_comment/<int:pk>/", reply_comment),
#     path("get_product_by_category/<int:pk>/", get_product_by_category),
#     path("get_product_by_subcategory/<int:pk>/", get_product_by_subcategory),
#     path("create_product/", create_product),
#     path("create_blog/", create_blog),
#     path("get_product/<int:pk>/", get_product),
#     path("wishlist_delete/<int:pk>/", wishlist_delete),
#     path("card_delete/<int:pk>/", card_delete),
#     path("update_card/<int:pk>/", update_card),
#     path("create_subscribers/", create_subscribers),
#     path("information/", information_view),
#     path("service/", service_view),
#     path("partner/", partner_view),
#     path("faq/", faq_view),
#     path("add_card/", add_card),
#     path("card_view/", card_view),
#     path("wishlist_view/", wishlist_view),
#     path("adress_view/", adress_view),
#     path("filter_product_price/", filter_product_price),
#     path("search_product_name/", search_product_name),
#     path("search_blog_name/", search_blog_name),
#     path("create_order/", create_order),
#     path("signin/", signin_view),
#     path("product_bunus_persent/", product_bunus_persent),
#     path("get_orderitem/<int:pk>/", get_orderitem),
#     path("get_client_orders/<int:pk>/", get_client_orders),
]