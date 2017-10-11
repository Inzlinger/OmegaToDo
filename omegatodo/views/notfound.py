from pyramid.view import view_config
from pyramid.security import Authenticated

@view_config(context='pyramid.exceptions.NotFound', renderer='omegatodo:templates/notfound.mako')
def notfound_view(request):
    request.response.status = '404 Not Found'
    return {}