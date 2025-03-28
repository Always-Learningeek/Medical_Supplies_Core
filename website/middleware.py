from django.shortcuts import redirect

COMING_SOON_MODE = True  # برای فعال یا غیرفعال کردن حالت

class ComingSoonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if COMING_SOON_MODE and not request.path.startswith('/coming-soon/'):
            return redirect('/coming-soon/')
        return self.get_response(request)