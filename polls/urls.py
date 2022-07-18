from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'polls', views.QuestionViewSet, basename='polls')

app_name = 'polls'
urlpatterns = [
	# using the old URLconf
	# # ex: /polls/
	# path('', views.index, name='index'),
	# # ex: /polls/5/
	# path('<int:question_id>/', views.detail, name='detail'),
	# # ex: /polls/5/results/
	# path('<int:question_id>/results/', views.results, name='results'),
	# # ex: /polls/5/vote/

	# changing URLconf --> newone
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),

	# for the rest API
	# path('', include(router.urls)),
	# path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + router.urls

