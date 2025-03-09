from django.urls import path
from .views import Home, InfoBook, about, contact, AddBook, EditBook, DeleteBook
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('infobook/<int:pk>/', InfoBook.as_view(), name='infobook'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('addbook/', AddBook.as_view(), name='addbook'),
    path('editbook/<int:pk>/', EditBook.as_view(), name='editbook'),
    path('deletebook/<int:pk>/', DeleteBook.as_view(), name='deletebook'),
    # path('search/', SearchBook.as_view(), name='search'),
]

