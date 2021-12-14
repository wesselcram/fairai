from django.urls import path

from . import views

urlpatterns = [
    path('', 					views.index, 				name='index'),
	path('toelichting', 		views.index, 				name='toelichting'),
	path('vragenlijst', 		views.vragenlijst, 			name='vragenlijst'),
	path('1411648771',	 		views.export_csv,	 		name='export_csv'),
]
