# context_processors.py

from master.models import Core

def core_data(request):
    core_data = Core.objects.filter(is_active=True).first()  # Or any other query you need
    return {'cores': core_data}
