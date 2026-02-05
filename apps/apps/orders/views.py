from django.http import JsonResponse
from .tasks import process_order

def create_order(request):
    task = process_order.delay(order_id=123)
    return JsonResponse({
        "message": "Order received",
        "task_id": task.id
    })
