from celery import shared_task

@shared_task(bind=True)
def process_order(self, order_id=None):
    print(f"Processing order: {order_id}")
    return {
        "status": "processed",
        "order_id": order_id
    }

@shared_task
def ping():
    return "pong"
