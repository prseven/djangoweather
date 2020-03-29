
from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode +"&distance=25&API_KEY=7190B714-04B6-4868-AEA1-D9792B57281E")
		
		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error...!!"


		return render(request, 'home.html', {'api': api})



	else:	
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=7190B714-04B6-4868-AEA1-D9792B57281E")
		
		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error...!!"


		return render(request, 'home.html', {'api': api})


def about(request):
	return render(request, 'about.html', {})
	
def index(request):
	return render(request, 'index.html', {})

	
	