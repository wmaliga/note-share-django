import json

from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from .models import Note
from .repository.note_repository import save


@csrf_exempt
def save_note(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        note = json.loads(request.body, object_hook=lambda d: Note.from_json(d))
        save(note)
        return HttpResponse(status=201)
    else:
        return HttpResponseBadRequest()
