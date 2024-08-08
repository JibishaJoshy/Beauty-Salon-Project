from django.urls import path
from Backend import views

urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('Addcategory_page/',views.Addcategory_page,name="Addcategory_page"),
    path('savedata_Category/',views.savedata_Category,name="savedata_Category"),
    path('Display_category/',views.Display_category, name="Display_category"),
    path('edit_category/<int:Categoryid>/',views.edit_category,name="edit_category"),
    path('update_category/<int:Categoryid>/',views.update_category,name="update_category"),
    path('delete_category/<int:Categoryid>/',views.delete_category,name="delete_category"),
    path('AddProducts_page/',views.AddProducts_page,name="AddProducts_page"),
    path('savedata_Products/',views.savedata_Products,name="savedata_Products"),
    path('display_Product/',views.display_Product, name="display_Product"),
    path('edit_products/<int:Productid>/',views.edit_products, name="edit_products"),
    path('login_page/',views.login_page,name="login_page"),
    path('login_admin/',views.login_admin,name="login_admin"),
    path('Adminlogout/',views.Adminlogout,name="Adminlogout"),
    path('update_products/<int:Productid>/',views.update_products,name="update_products"),



    path('Contact_Details/',views.Contact_Details,name="Contact_Details"),
    path('delete_contact/<int:Contactid>/',views.delete_contact,name="delete_contact"),


]