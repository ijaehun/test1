from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import RegionModel, S, R1, R2, R3, R4, R5, R6, schooldata_by_professer_babies, all_schools_by_year, all_students_by_year
# from nameapp.models import KospiPredict
from django.views.generic import View
from time import mktime, strptime
import folium
import geopandas as gpd
import pandas as pd
import csv
from rest_framework.renderers import TemplateHTMLRenderer
from django.template.response import TemplateResponse
from django.conf import settings
import os
from django.http import HttpResponse
from django.http import JsonResponse
import json


class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/login.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class RegisterView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/register.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ForgotPasswordView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ChartsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/charts.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class TablesView(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/신생아수 예측.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data,
                   'series1_name': '통계청',
                   'series2_name': '저위',
                   'series3_name': '중위',
                   'series4_name': 'CRU',
                   'series5_name': 'SSM}'}
        
        return render(request, "theme/tables.html", context)
        
class TablesView1(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/저위추계_학생수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}
        
        return render(request, "theme/tables1.html", context) 

class TablesView1_1(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/무이동추계_학생수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}
        
        return render(request, "theme/tables1_1.html", context) 

class TablesView2(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/중위추계_학생수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}
        
        return render(request, "theme/tables2.html", context) 
    
class TablesView3(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/CRU_학생수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables3.html", context)
    
class TablesView4(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/SSM_학생수.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables4.html", context)
    

class TablesView5(APIView):
    def get(self, request, *args, **kwargs):
        results = R6.objects.all()
        return render(request, "theme/tables5.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView5_results(APIView):    
        def get(self, request, *args, **kwargs):
            schoollevel = request.GET['schoollevel']
            prelevel = request.GET['prelevel']
            model = request.GET['model']

            df = pd.read_csv(f"./적정교원산출연구/저위/{schoollevel}_{prelevel}_{model}.csv",encoding="utf-8-sig")

            list1 = [schoollevel, prelevel]

            json_records = df.to_json(orient ='records')
            data = json.loads(json_records)

            return render(request, "theme/tables5_results.html", {'df': data, 'l':list1})


class TablesView5_1(APIView):
    def get(self, request, *args, **kwargs):
        results = R6.objects.all()
        return render(request, "theme/tables5_1.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView5_1_results(APIView):    
        def get(self, request, *args, **kwargs):
            schoollevel = request.GET['schoollevel']
            prelevel = request.GET['prelevel']
            model = request.GET['model']

            df = pd.read_csv(f"./적정교원산출연구/무이동/{schoollevel}_{prelevel}_{model}.csv",encoding="utf-8-sig")

            list1 = [schoollevel, prelevel]

            json_records = df.to_json(orient ='records')
            data = json.loads(json_records)

            return render(request, "theme/tables5_1_results.html", {'df': data, 'l':list1})


class TablesView6(APIView):
    def get(self, request, *args, **kwargs):
        results = R6.objects.all()
        return render(request, "theme/tables6.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView6_results(APIView):    
        def get(self, request, *args, **kwargs):
            schoollevel = request.GET['schoollevel']
            prelevel = request.GET['prelevel']
            model = request.GET['model']

            df = pd.read_csv(f"./적정교원산출연구/중위/{schoollevel}_{prelevel}_{model}.csv",encoding="utf-8-sig")

            list1 = [schoollevel, prelevel]

            json_records = df.to_json(orient ='records')
            data = json.loads(json_records)

            return render(request, "theme/tables6_results.html", {'df': data, 'l':list1})


class TablesView7(APIView):
    def get(self, request, *args, **kwargs):
        results = R6.objects.all()
        return render(request, "theme/tables7.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView7_results(APIView):    
        def get(self, request, *args, **kwargs):
            schoollevel = request.GET['schoollevel']
            prelevel = request.GET['prelevel']

            df = pd.read_csv(f"./적정교원산출연구/CRU/{schoollevel}_{prelevel}.csv",encoding="utf-8-sig")

            list1 = [schoollevel, prelevel]

            json_records = df.to_json(orient ='records')
            data = json.loads(json_records)

            return render(request, "theme/tables7_results.html", {'df': data, 'l':list1})


class TablesView8(APIView):
    def get(self, request, *args, **kwargs):
        results = R6.objects.all()
        return render(request, "theme/tables8.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    

class TablesView8_results(APIView):    
        def get(self, request, *args, **kwargs):
            schoollevel = request.GET['schoollevel']
            prelevel = request.GET['prelevel']

            df = pd.read_csv(f"./적정교원산출연구/SSM/{schoollevel}_{prelevel}.csv",encoding="utf-8-sig")

            list1 = [schoollevel, prelevel]

            json_records = df.to_json(orient ='records')
            data = json.loads(json_records)

            return render(request, "theme/tables8_results.html", {'df': data, 'l':list1})


class TablesView9(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/초등학교_저위추계_학급수_기본.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables9.html", context)

class TablesView9_1(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/초등학교_저위추계_학급수_공동주택.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables9_1.html", context)

class TablesView9_2(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/초등학교_무이동추계_학급수_기본.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables9_2.html", context)

class TablesView9_3(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/초등학교_무이동추계_학급수_공동주택.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables9_3.html", context)

class TablesView9_4(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/초등학교_중위추계_학급수_기본.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables9_4.html", context)

class TablesView9_5(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/초등학교_중위추계_학급수_공동주택.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables9_5.html", context)


class TablesView10(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/초등학교_CRU_학급수.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables10.html", context)

    
class TablesView11(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/초등학교_SSM_학급수.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables11.html", context)


class TablesView12(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/중학교_중위추계_학급수.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables12.html", context)

class TablesView12_1(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/중학교_중위추계_학급수.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables12_1.html", context)

class TablesView12_2(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/중학교_중위추계_학급수.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables12_2.html", context)


class TablesView13(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/중학교_CRU_학급수.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables13.html", context)
    
class TablesView14(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/중학교_SSM_학급수.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables14.html", context)
    
class TablesView15(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/고등학교_중위추계_학급수.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables15.html", context)

class TablesView15_1(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/고등학교_중위추계_학급수.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables15_1.html", context)

class TablesView15_2(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/고등학교_중위추계_학급수.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables15_2.html", context)


class TablesView16(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/고등학교_CRU_학급수.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables16.html", context)
    

class TablesView17(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/학급수/고등학교_SSM_학급수.csv",encoding="utf-8-sig")
        
        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data}

        return render(request, "theme/tables17.html", context)


class TablesView18(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/초등학교_저위추계_교원수_기본.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables18.html", context)

class TablesView18_1(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/초등학교_저위추계_교원수_공동주택.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables18_1.html", context)

class TablesView18_2(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/초등학교_무이동추계_교원수_기본.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables18_2.html", context)

class TablesView18_3(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/초등학교_무이동추계_교원수_공동주택.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables18_3.html", context)

class TablesView18_4(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/초등학교_중위추계_교원수_기본.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables18_4.html", context)

class TablesView18_5(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/초등학교_중위추계_교원수_공동주택.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables18_5.html", context)


class TablesView19(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/초등학교_CRU_교원수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables19.html", context)


class TablesView20(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/초등학교_SSM_교원수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables20.html", context)


class TablesView21(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/중학교_중위추계_교원수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables21.html", context)

class TablesView21_1(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/중학교_중위추계_교원수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables21_1.html", context)

class TablesView21_2(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/중학교_중위추계_교원수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables21_2.html", context)


class TablesView22(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/중학교_CRU_교원수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables22.html", context)
    

class TablesView23(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/중학교_SSM_교원수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables23.html", context)  

class TablesView24(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/고등학교_중위추계_교원수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables24.html", context)

class TablesView24_1(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/고등학교_중위추계_교원수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables24_1.html", context)

class TablesView24_2(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/고등학교_중위추계_교원수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables24_2.html", context)


class TablesView25(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/고등학교_CRU_교원수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables25.html", context)

class TablesView26(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./적정교원산출연구/교원수/고등학교_SSM_교원수.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        return render(request, "theme/tables26.html", context)        

        

class uTablesView17_1(APIView):
        def get(self, request):
            
            return render(request, "theme/utables17_1.html")

class uTablesView18_1(APIView):
    def get(self, request):
            
            return render(request, "theme/utables18_1.html")

class uTablesView19_1(APIView):
    def get(self, request):
            
            return render(request, "theme/utables19_1.html")

class uTablesView20_1(APIView):
    def get(self, request):
            
            return render(request, "theme/utables20_1.html")

class uTablesView21_1(APIView):
    def get(self, request):
            
            return render(request, "theme/utables21_1.html")

class uTablesView22_1(APIView):
    def get(self, request):
            
            return render(request, "theme/utables22_1.html")

class uTablesView23_1(APIView):
    def get(self, request):
            
            return render(request, "theme/utables23_1.html")                            


class uTablesView24_1(APIView):
    def get(self, request):
            
            return render(request, "theme/utables24_1.html")




class simulation_count_url(APIView):
    def get(self, request):
        
        return render(request, 'theme/simulation_count_url.html',{})

        

class simulation_count_results_url(APIView):
    
    def get(self, request, *args, **kwargs):
        schoollevel = request.GET['schoollevel']
        prelevel = request.GET['prelevel']
        start_num = request.GET['start_num']
        #end_num = request.GET['end_num']
        limit = request.GET['limit']

        end_num = int(start_num) + 9
        end_num = "년" + str(end_num)
        start_num = "년" + str(start_num)
        

        
        df = pd.read_csv("./예측인원.csv",encoding="utf-8-sig")
        data1 = df[(df["학교유형"]==schoollevel)&(df["예측유형"]==prelevel)]
        data2 = data1.loc[:,"학교명"]
        data3 = data1.loc[:,start_num:end_num]
        data4 = data1.loc[:,"SIG_KOR_NM"]
        data5 = data1.loc[:,"SIG_CD"]

        if (schoollevel=="초등학교"):
            data3 = round(5.939 + 1.404*(data3/int(limit)))
        elif(schoollevel=="중학교"):
            data3 = round(7.701 + 1.720*(data3/int(limit)))
        elif(schoollevel=="고등학교"):
            data3 = round(11.473 + 1.941*(data3/int(limit)))
        
        data = pd.concat([data2,data3,data4,data5],axis=1)

        if (len(data3.columns)==1):
            data.columns = ["학교명","필요교원수","SIG_KOR_NM","SIG_CD"]
        elif (len(data3.columns)==2):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==3):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==4):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==5):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==6):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==7):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==8):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==9):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==10):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        

        return render(request, "theme/simulation_count_results_url.html", context)

# class simulation_close_url(APIView):
#     def get(self, request, *args, **kwargs):
#         results = R6.objects.all()
#         return render(request, "theme/simulation_close_url.html", {'results':results})

#     def post(self, request, *args, **kwargs):

#         return Response({'status': 200})

# class simulation_close_results_url(APIView):
    
#     def get(self, request, *args, **kwargs):
#         schoollevel = request.GET['schoollevel']
#         prelevel = request.GET['prelevel']
#         start_num = request.GET['start_num']
        
#         end_num = int(start_num) + 9
#         end_num = "년" + str(end_num)
#         start_num = "년" + str(start_num)
        
#         df = pd.read_csv("./예측인원.csv",encoding="utf-8-sig")
#         data1 = df[(df["학교유형"]==schoollevel)&(df["예측유형"]==prelevel)]
#         data2 = data1.loc[:,"학교명"]
#         data3 = data1.loc[:,start_num:end_num]
#         data4 = data1.loc[:,"SIG_KOR_NM"]
#         data5 = data1.loc[:,"SIG_CD"]

#         data = pd.concat([data2,data3,data4,data5],axis=1)

#         results = []

#         for i in range(len(data3.columns)):
#             ff = data[data[data3.columns[i]]==0]["학교명"].count()
#             results.append(ff)        

#         data = pd.DataFrame(results).T

#         ff = []
        
#         for i in range(len(data3.columns)):
#             ff.append("필요교원수"+f"{i}")
        

#         data.columns = ff

#         json_records = data.to_json(orient ='records')
#         data = json.loads(json_records)
#         context = {'df': data}
        
#         return render(request, "theme/simulation_close_results_url.html", context)

class simulation_close_url(APIView):
    def get(self, request, *args, **kwargs):
        results = R6.objects.all()
        return render(request, "theme/simulation_close_url.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

class simulation_close_results_url(APIView):

    def get(self, request, *args, **kwargs):
        schoollevel = request.GET['schoollevel']
        prelevel = request.GET['prelevel']
        
        df = pd.read_csv(f"./적정교원산출연구/05. 적정교원배치결과/{schoollevel}_{prelevel}.csv",encoding="utf-8-sig")
        list1 = [schoollevel, prelevel]
        
        json_records = df.to_json(orient ='records')
        data = json.loads(json_records)

        return render(request, "theme/simulation_close_results_url.html", {'df': data, 'l':list1})
    

    
# class simulation_close_results_url(APIView):
    
#     def get(self, request, *args, **kwargs):
#         schoollevel = request.GET['schoollevel']
#         prelevel = request.GET['prelevel']
#         start_num = request.GET['start_num']
        
#         end_num = int(start_num) + 9
#         end_num = "년" + str(end_num)
#         start_num = "년" + str(start_num)
        
#         df = pd.read_csv("./예측인원.csv",encoding="utf-8-sig")
#         data1 = df[(df["학교유형"]==schoollevel)&(df["예측유형"]==prelevel)]
#         data2 = data1.loc[:,"학교명"]
#         data3 = data1.loc[:,start_num:end_num]
#         data4 = data1.loc[:,"SIG_KOR_NM"]
#         data5 = data1.loc[:,"SIG_CD"]

#         data = pd.concat([data2,data3,data4,data5],axis=1)

#         results = []

#         for i in range(len(data3.columns)):
#             ff = data[data[data3.columns[i]]==0]["학교명"].count()
#             results.append(ff)        

#         data = pd.DataFrame(results).T

#         ff = []
        
#         for i in range(len(data3.columns)):
#             ff.append("필요교원수"+f"{i}")
        

#         data.columns = ff

#         json_records = data.to_json(orient ='records')
#         data = json.loads(json_records)
#         context = {'df': data}
        
#         return render(request, "theme/simulation_close_results_url.html", context)
      
   
class IndexView(APIView):
    def visualize_csv(request):
    # CSV 파일 경로 설정
        csv_file_path = './src/csv/년도별_총학교수_csv.csv'

    # CSV 파일 읽기
        with open(csv_file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            data = list(reader)

            labels = [row[0] for row in data[1:]]
            values = [int(row[1]) for row in data[1:]]

    # HTML 파일 렌더링
        return render(request, 'theme/simulation_close.html', {'labels': labels, 'values': values})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class indexview2(APIView):
    def get(self, request, *args, **kwargs):
        results = all_students_by_year.objects.all()
        return render(request, "theme/index.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
# class KospiPredictAPIView(APIView):

#     authentication_classes = []
#     permission_classes = []

#     def get(self, request):
#         stocks = KospiPredict.objects.all().order_by('date')

#         close_list = []
#         open_list = []
#         for stock in stocks:
#             time_tuple = strptime(str(stock.date), '%Y-%m-%d')  
#             utc_now = mktime(time_tuple) * 1000           
#             close_list.append([utc_now, stock.close])
#             open_list.append([utc_now, stock.open])

#         data = {
#             'close': close_list,
#             'open': open_list
#         }

#         return Response(data)

class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'nameapp/chart.html')

class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ButtonsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/buttons.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class CardsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/cards.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class PageNotFoundView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/404.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class BlankView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/blank.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ColorsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-color.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class BordersView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-border.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class AnimationsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-animation.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class OthersView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-other.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})



class DashboardView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "users/dashboard.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

class Map_View(APIView): #시각화 날리는
    def get(self, request, *args, **kwargs):
        gdf = gpd.read_file('./geo/daegu_gu_4326.shp')
        
        data = pd.read_csv("./test2.csv")
        data['일3년'] = data['일3년'].astype(object)
        m = folium.Map(location=[35.85788, 128.58918], zoom_start=9)

        cp = folium.Choropleth(geo_data=gdf,
                          name="2010",
                          data=data,
                          key_on='feature.properties.SIG_CD',
                          columns=['SIG_CD', '일3년'],
                          fill_color='YlOrRd',
                          fill_opacity=0.5,
                          line_opacity=0.7,
                          legend_name='학교수',
                          highlight=True).add_to(m)
        
        data_indexed = data.set_index('SIG_KOR_NM')

        for s in cp.geojson.data['features']:
             s['properties']['2010년'] = data_indexed.loc[s['properties']['SIG_KOR_NM'], '일3년']
  
        folium.GeoJsonTooltip(['SIG_KOR_NM', '2010년']).add_to(cp.geojson)
        
        # 툴팁(hover) 추가
        # folium.GeoJsonTooltip(
        #     fields=['SIG_KOR_NM','2010년'],  # 툴팁에 표시할 열 지정
        #     aliases=['행정구 :','학교수 :'],  # 툴팁 열에 대한 별칭 지정
        #     style=('font-weight: bold;')  # 툴팁 스타일 지정
        # ).add_to(cp.geojson)

        folium.LayerControl().add_to(m)
        #folium.GeoJson(gdf).add_to(m)

        m = m._repr_html_()
        
        return render(request, "theme/map.html", {'map':m})

class Map_View2(APIView): #인덱스
    def get(self, request, *args, **kwargs):
        gdf = gpd.read_file('./geo/daegu_gu_4326.shp')
        
        data = pd.read_csv("./test2.csv")
        data['일3년'] = data['일3년'].astype(object)
        m = folium.Map(location=[35.85788, 128.58918], zoom_start=9)

        cp = folium.Choropleth(geo_data=gdf,
                          name="2010",
                          data=data,
                          key_on='feature.properties.SIG_CD',
                          columns=['SIG_CD', '일3년'],
                          fill_color='YlOrRd',
                          fill_opacity=0.5,
                          line_opacity=0.7,
                          legend_name='학교수',
                          highlight=True).add_to(m)
        
        data_indexed = data.set_index('SIG_KOR_NM')

        for s in cp.geojson.data['features']:
             s['properties']['2010년'] = data_indexed.loc[s['properties']['SIG_KOR_NM'], '일3년']
  
        folium.GeoJsonTooltip(['SIG_KOR_NM', '2010년']).add_to(cp.geojson)
        
        # 툴팁(hover) 추가
        # folium.GeoJsonTooltip(
        #     fields=['SIG_KOR_NM','2010년'],  # 툴팁에 표시할 열 지정
        #     aliases=['행정구 :','학교수 :'],  # 툴팁 열에 대한 별칭 지정
        #     style=('font-weight: bold;')  # 툴팁 스타일 지정
        # ).add_to(cp.geojson)

        folium.LayerControl().add_to(m)
        #folium.GeoJson(gdf).add_to(m)

        m = m._repr_html_()

        return render(request, "theme/index.html", {'map':m})
    
