from django.urls import path
from Webapp import views

urlpatterns=[
    path('',views.homepage,name="home"),
    path('About/',views.Aboutpage,name="About"),
    path('Workspage/',views.Workspage,name="Workspage"),
    path('Contactpage/',views.Contactpage,name="Contactpage"),
    path('savedata_Contact/',views.savedata_Contact,name="savedata_Contact"),
    path('Filtered_Services/<categ_name>/',views.Filtered_Services,name="Filtered_Services"),
    path('Single_Productpage/<int:prod_id>/',views.Single_Productpage,name="Single_Productpage"),

    path('CartPage/',views.CartPage,name="CartPage"),
    path('save_Cart/', views.save_Cart, name="save_Cart"),

# *************************************
    path('Booking_page/',views.Booking_page,name="Booking_page"),
    path('Order_page/',views.Order_page,name="Order_page"),
    # ***********************
    # path('pricing/', pricing_view, name='pricing'),
    # *******************

    path('Registration_page/',views.Registration_page,name="Registration_page"),
    path('save_Register/',views.save_Register,name="save_Register"),
    path('Loginpg/',views.Loginpg,name="Loginpg"),
    path('UserLogin/',views.UserLogin,name="UserLogin"),
    path('UserLogout/',views.UserLogout,name="UserLogout"),

    path('save_Cart/',views.save_Cart,name="save_Cart"),
    path('CartPage/',views.CartPage,name="CartPage"),
    path('delete_item/<int:p_id>/', views.delete_item, name="delete_item"),

    path('CheckOut/',views.CheckOut,name="CheckOut"),
    path('SaveOrder/',views.SaveOrder,name="SaveOrder"),
]
