from datetime import datetime

def datetime_now(request):
    now = datetime.now()
    return {'now':now}