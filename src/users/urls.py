from django.urls import re_path, path , include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "users"


urlpatterns = [
   	# Login, Register, Forgot password, Logout
    re_path(r'^login/$', views.LoginView.as_view(), name="login_url"),
    re_path(r'^register/$', views.RegisterView.as_view(), name="register_url"),
    re_path(r'^forgot-password/$', views.ForgotPasswordView.as_view(), name="forgot_password_url"),
    re_path(r'^logout/$', views.LogoutView.as_view(), name="logout_url"),

    re_path(r'^charts/$', views.ChartsView.as_view(), name="charts_url"),

    re_path(r'^tables/$', views.TablesView.as_view(), name="tables_url"),
    re_path(r'^tables1/$', views.TablesView1.as_view(), name="tables1_url"),
    re_path(r'^tables1_1/$', views.TablesView1_1.as_view(), name="tables1_1_url"),

    re_path(r'^tables2/$', views.TablesView2.as_view(), name="tables2_url"),
    re_path(r'^tables3/$', views.TablesView3.as_view(), name="tables3_url"),
    re_path(r'^tables4/$', views.TablesView4.as_view(), name="tables4_url"),

    re_path(r'^tables5/$', views.TablesView5.as_view(), name="tables5_url"),
    re_path(r'^tables5_results/$', views.TablesView5_results.as_view(), name="tables5_results_url"),

    re_path(r'^tables6/$', views.TablesView6.as_view(), name="tables6_url"),
    re_path(r'^tables6_results/$', views.TablesView6_results.as_view(), name="tables6_results_url"),

    re_path(r'^tables7/$', views.TablesView7.as_view(), name="tables7_url"),
    re_path(r'^tables7_results/$', views.TablesView7_results.as_view(), name="tables7_results_url"),

    re_path(r'^tables8/$', views.TablesView8.as_view(), name="tables8_url"),
    re_path(r'^tables8_results/$', views.TablesView8_results.as_view(), name="tables8_results_url"),

    re_path(r'^tables9/$', views.TablesView9.as_view(), name="tables9_url"),
    re_path(r'^tables10/$', views.TablesView10.as_view(), name="tables10_url"),
    re_path(r'^tables11/$', views.TablesView11.as_view(), name="tables11_url"),
    re_path(r'^tables12/$', views.TablesView12.as_view(), name="tables12_url"),
    re_path(r'^tables13/$', views.TablesView13.as_view(), name="tables13_url"),
    re_path(r'^tables14/$', views.TablesView14.as_view(), name="tables14_url"),
    re_path(r'^tables15/$', views.TablesView15.as_view(), name="tables15_url"),
    re_path(r'^tables16/$', views.TablesView16.as_view(), name="tables16_url"),
    re_path(r'^tables17/$', views.TablesView17.as_view(), name="tables17_url"),
    re_path(r'^tables18/$', views.TablesView18.as_view(), name="tables18_url"),
    re_path(r'^tables19/$', views.TablesView19.as_view(), name="tables19_url"),
    re_path(r'^tables20/$', views.TablesView20.as_view(), name="tables20_url"),
    re_path(r'^tables21/$', views.TablesView21.as_view(), name="tables21_url"),
    re_path(r'^tables22/$', views.TablesView22.as_view(), name="tables22_url"),
    re_path(r'^tables23/$', views.TablesView23.as_view(), name="tables23_url"),
    re_path(r'^tables24/$', views.TablesView24.as_view(), name="tables24_url"),
    re_path(r'^tables25/$', views.TablesView25.as_view(), name="tables25_url"),
    re_path(r'^tables26/$', views.TablesView26.as_view(), name="tables26_url"),


    re_path(r'^utables17_1/$', views.uTablesView17_1.as_view(), name="utables17_1_url"),
    re_path(r'^utables18_1/$', views.uTablesView18_1.as_view(), name="utables18_1_url"),
    re_path(r'^utables19_1/$', views.uTablesView19_1.as_view(), name="utables19_1_url"),
    re_path(r'^utables20_1/$', views.uTablesView20_1.as_view(), name="utables20_1_url"),
    re_path(r'^utables21_1/$', views.uTablesView21_1.as_view(), name="utables21_1_url"),
    re_path(r'^utables22_1/$', views.uTablesView22_1.as_view(), name="utables22_1_url"),
    re_path(r'^utables23_1/$', views.uTablesView23_1.as_view(), name="utables23_1_url"),
    re_path(r'^utables24_1/$', views.uTablesView24_1.as_view(), name="utables24_1_url"),

    
    re_path(r'^simulation_count_url/$', views.simulation_count_url.as_view(), name="simulation_count_url"),
    re_path(r'^simulation_count_results_url/$', views.simulation_count_results_url.as_view(), name="simulation_count_results_url"),

    re_path(r'^simulation_close_url/$', views.simulation_close_url.as_view(), name="simulation_close_url"),
    re_path(r'^simulation_close_results_url/$', views.simulation_close_results_url.as_view(), name="simulation_close_results_url"),

    re_path(r'^buttons/$', views.ButtonsView.as_view(), name="buttons_url"),

    re_path(r'^cards/$', views.CardsView.as_view(), name="cards_url"),

	re_path(r'^page_not_found/$', views.PageNotFoundView.as_view(), name="page_not_found_url"),    

	re_path(r'^blank/$', views.BlankView.as_view(), name="blank_page_url"),    

	# Utilities
	re_path(r'^colors/$', views.ColorsView.as_view(), name="colors_url"),    

	re_path(r'^borders/$', views.BordersView.as_view(), name="borders_url"),    

	re_path(r'^animations/$', views.AnimationsView.as_view(), name="animations_url"),    

	re_path(r'^others/$', views.OthersView.as_view(), name="others_url"),    

    re_path(r'^map/$', views.Map_View.as_view(), name="map_view_url"),
    re_path(r'^map/$', views.Map_View2.as_view(), name="index_url"),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)