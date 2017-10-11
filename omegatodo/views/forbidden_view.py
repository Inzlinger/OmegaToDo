from pyramid.view import forbidden_view_config
from pyramid.security import Authenticated
from pyramid.httpexceptions import  HTTPFound

@forbidden_view_config()
def forbidden_view(request):
    request.session.flash('Zugriff nicht gestattet, bitte melden Sie sich an!')
    return HTTPFound(location=request.route_url('welcome'))