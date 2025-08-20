import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from ..models import PredeterminedPrice

@csrf_exempt
def predetermined_prices_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    qs = PredeterminedPrice.objects.all()
    data = [{"id": x.id, "name": x.name, "price": str(x.price)} for x in qs]
    return JsonResponse({"predetermined_prices": data})

@csrf_exempt
def predetermined_price_create(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    payload = json.loads(request.body.decode() or "{}")
    pp = PredeterminedPrice.objects.create(name=payload.get("name",""), price=payload.get("price"))
    return JsonResponse({"id": pp.id, "name": pp.name, "price": str(pp.price)}, status=201)
