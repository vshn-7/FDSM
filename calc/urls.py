from this import s
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home, name='home'),path('login',views.login, name='login'), path('Amigos',views.Amigos,name='Amigos'),
    path('PFC',views.PFC,name='PFC'),path('CityBites',views.CityBites,name='CityBites'),  path('BillA',views.BillA,name='BillA'), 
    path('BillP',views.BillP,name='BillP'), path('BillC',views.BillC,name='BillC'),path('BillH',views.BillH,name='BillH'), path('edit',views.edit,name='edit'),
    path('requests',views.requests,name='requests'),path('stats',views.stats,name='stats'), path('user',views.user,name='user'),
    path('signup',views.signup,name='signup'), path('edit1',views.edit1,name="edit1"), path('edit2',views.edit2,name="edit2"),
    path('edit3',views.edit3,name="edit3"),path('BillM',views.BillM,name='BillM'),
    path('Heritage',views.Heritage,name='Heritage'),path('Miamore',views.Miamore,name='Miamore'),path('edit4',views.edit4,name="edit4"),
    path('create',views.create,name="create"),path('stats1',views.stats1,name='stats1'),path('stats2',views.stats2,name='stats2'),
    path('stats3',views.stats3,name='stats3'), path('stats4',views.stats4,name='stats4'), path('edittax',views.edittax,name='edittax'),
    path('back',views.back,name='back'),path('save',views.save,name='save'), path('logout',views.logout,name='logout'),
    path('seecus',views.seecus,name='seecus'), path('seeres',views.seeres,name='seeres'), path('review1',views.review1,name='review1'),
    path('review2',views.review2,name='review2'),path('review3',views.review3,name='review3'),
    path('review4',views.review4,name='review4'),
    path('review5',views.review5,name='review5'),path('requests1',views.requests1,name='requests1'),path('requests2',views.requests2,name='requests2'),
    path('requests4',views.requests4,name='requests4'),path('requests3',views.requests3,name='requests3'),
    path('back1',views.back1,name='back1'),path('back2',views.back2,name='back2'),path('back3',views.back3,name='back3'),
    path('back4',views.back4,name='back4'),path('back5',views.back5,name='back5'),path('back6',views.back6,name='back6'),
    path('back7',views.back7,name='back7'),path('back8',views.back8,name='back8'),path('back9',views.back9,name='back9'),
    path('back10',views.back10,name='back10'),path('back11',views.back11,name='back11'),path('statsMa',views.statsMa,name='statsMa'),
    path('statsMp',views.statsMp,name='statsMp'),path('statsMc',views.statsMc,name='statsMc'),path('statsMh',views.statsMh,name='statsMh'),
    path('statsMm',views.statsMm,name='statsMm'), path('back12',views.back12,name='back12'),path('back13',views.back13,name='back13'),
    path('prevorders',views.prevorders,name='prevorders'),path('back14',views.back14,name='back14'),
    path('back15',views.back15,name='back15'),
    path('printbill1',views.printbill1,name='printbill1'),path('printbill2',views.printbill2,name='printbill2'),
    path('printbill3',views.printbill3,name='printbill3'),path('printbill4',views.printbill4,name='printbill4'),
    path('printbill5',views.printbill5,name='printbill5'), path('create1',views.create1,name="create1"),
    path('seedel',views.seedel,name='seedel'),
]
urlpatterns += staticfiles_urlpatterns()