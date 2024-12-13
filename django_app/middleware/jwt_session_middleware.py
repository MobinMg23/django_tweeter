from django.utils.deprecation import MiddlewareMixin

class JWTSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # بررسی وجود توکن در session
        access_token = request.session.get('access_token')
        if access_token:
            # افزودن توکن به هدر Authorization
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
        else:
            print("Access token not found in session")