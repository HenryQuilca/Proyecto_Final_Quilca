from django.contrib.auth.views import LogoutView
from django.urls import path
from AppQuilca.views import RacquetCreate, buscar_racquet, RacquetList, home, RacquetDetail, RacquetUpdate, \
    RacquetDelete, log_in, sing_up, edit_profile, about_me, editar_avatar_request, CommentCreate

urlpatterns = [
    path('home/', home, name="Home"),
    path('about_me/', about_me),
    path('buscar_racquet/', buscar_racquet),
    path('crear_raqueta/', RacquetCreate.as_view(), name="RacquetCreate"),
    path('listar_raquetas/', RacquetList.as_view(), name="RacquetList"),
    path('detalle_raquetas/<int:pk>', RacquetDetail.as_view(), name="RacquetDetail"),
    path('editar_raquetas/<int:pk>', RacquetUpdate.as_view(), name="RacquetUpdate"),
    path('eliminar_raquetas/<int:pk>', RacquetDelete.as_view(), name="RacquetDelete"),
    path('log_in/', log_in, name="Login"),
    path('log_out/', LogoutView.as_view(template_name="AppQuilca/logout.html"), name="Logout"),
    path('sing_up/', sing_up, name="Singup"),
    path('edit_profile/', edit_profile, name="Edit"),
    path('avatar/', editar_avatar_request, name="Avatar"),
    path('comentario/', CommentCreate.as_view(), name="Comment"),
    path('comentario/<int:raqueta_id>/', CommentCreate.as_view(), name='comentario'),
]
