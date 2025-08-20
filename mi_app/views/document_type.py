import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from ..models import DocumentType

@csrf_exempt
def document_types_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    qs = DocumentType.objects.filter(deleted_at__isnull=True)
    data = [{"id": x.id, "name": x.name, "description": x.description} for x in qs]
    return JsonResponse({"document_types": data})

@csrf_exempt
def document_type_create(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    payload = json.loads(request.body.decode() or "{}")
    dt = DocumentType.objects.create(name=payload.get("name",""), description=payload.get("description"))
    return JsonResponse({"id": dt.id, "name": dt.name, "description": dt.description}, status=201)

@csrf_exempt
def document_type_delete(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    try:
        dt = DocumentType.objects.get(pk=pk, deleted_at__isnull=True)
    except DocumentType.DoesNotExist:
        return JsonResponse({"error":"No encontrado"}, status=404)
    dt.soft_delete()
    return JsonResponse({"status": "deleted"})
