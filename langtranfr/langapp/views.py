from django.shortcuts import render

# Create your views here.
# myapp/views.py

from django.shortcuts import render
from django.utils.translation import gettext as _

def my_view(request, language):
    # Set language for this view
    request.session['django_language'] = language

    # Your content here
    content = _("Hello, this is some content.")

    return render(request, 'my_template.html', {'content': content})


# views.py

from django.http import JsonResponse
from django.utils import translation
from django.views.decorators.http import require_POST

@require_POST
def change_language(request):
    language_code = request.POST.get('language', 'en')
    translation.activate(language_code)
    request.session[translation.LANGUAGE_SESSION_KEY] = language_code
    return JsonResponse({'success': True})
