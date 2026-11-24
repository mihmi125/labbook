from django.shortcuts import render

# Create your views here.
def resource_list(request):
    resources = [
        {"id": 1, "name": "FortiGate 60E", "category": "Võrguseade"},
        {"id": 2, "name": "Cisco ISR", "category": "Võrguseade"},
        {"id": 3, "name": "Projektor", "category": "Esitlustehnika"},
    ]
    return render(request, "catalog/resources.html", {"resources": resources})