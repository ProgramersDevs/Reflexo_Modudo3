import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from ..models import PaymentType

@csrf_exempt
def payment_types_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    qs = PaymentType.objects.filter(deleted_at__isnull=True)
    data = [{"id": x.id, "code": x.code, "name": x.name} for x in qs]
    return JsonResponse({"payment_types": data})

@csrf_exempt
def payment_type_create(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    payload = json.loads(request.body.decode() or "{}")
    pt = PaymentType.objects.create(code=payload.get("code",""), name=payload.get("name",""))
    return JsonResponse({"id": pt.id, "code": pt.code, "name": pt.name}, status=201)

@csrf_exempt
def payment_type_delete(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    try:
        pt = PaymentType.objects.get(pk=pk, deleted_at__isnull=True)
    except PaymentType.DoesNotExist:
        return JsonResponse({"error":"No encontrado"}, status=404)
    pt.soft_delete()
    return JsonResponse({"status": "deleted"})
