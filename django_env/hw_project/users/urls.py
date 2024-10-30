from django.urls import path
from users.views import signupuser, loginuser, logoutuser, profile

app_name = 'users'

urlpatterns = [
    path('signup/', signupuser, name='signup'),
    path('login/', loginuser, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('profile/', profile, name='profile'),

 # Маршруты для цитат
    path('', quote_views.home, name='home'),  # Главная страница с цитатами
    path('quotes/', quote_views.quotes_list, name='quotes_list'),  # Список всех цитат
    path('quotes/<int:quote_id>/', quote_views.quote_detail, name='quote_detail'),  # Подробная информация о конкретной цитате
    path('author/<str:author>/', quote_views.author_quotes, name='author_quotes'),  # Цитаты конкретного автора
    path('tags/', quote_views.tags_list, name='tags_list'),  # Список всех тегов
    path('tag/<str:tag>/', quote_views.tag_quotes, name='tag_quotes'),  # Цитаты по тегу

]






# from django.urls import path
# from users import views as user_views
# from quotes import views as quote_views

# app_name = 'main'

# urlpatterns = [
#     # Маршруты для управления пользователями
#     path('signup/', user_views.signupuser, name='signup'),
#     path('login/', user_views.loginuser, name='login'),
#     path('logout/', user_views.logoutuser, name='logout'),
#     path('profile/', user_views.profile, name='profile'),

#     # Маршруты для цитат
#     path('', quote_views.home, name='home'),  # Главная страница с цитатами
#     path('quotes/', quote_views.quotes_list, name='quotes_list'),  # Список всех цитат
#     path('quotes/<int:quote_id>/', quote_views.quote_detail, name='quote_detail'),  # Подробная информация о конкретной цитате
#     path('author/<str:author>/', quote_views.author_quotes, name='author_quotes'),  # Цитаты конкретного автора
#     path('tags/', quote_views.tags_list, name='tags_list'),  # Список всех тегов
#     path('tag/<str:tag>/', quote_views.tag_quotes, name='tag_quotes'),  # Цитаты по тегу
# ]














# from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
# from django.urls import path
# from users import views

# app_name = 'users'

# urlpatterns = [
#     path('signup/', views.signupuser, name='signup'),
#     path('login/', views.loginuser, name='login'),
#     path('logout/', views.logoutuser, name='logout'),
#     path('profile/', views.profile, name='profile'),
#     path('reset-password/', views.ResetPasswordView.as_view(), name='password_reset'),
#     path('reset-password/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
#          name='password_reset_done'),
#     path('reset-password/confirm/<uidb64>/<token>/',
#          PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
#                                           success_url='/users/reset-password/complete/'),
#          name='password_reset_confirm'),
#     path('reset-password/complete/',
#          PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
#          name='password_reset_complete'),
# ]