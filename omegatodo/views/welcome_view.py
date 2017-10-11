from pyramid.view import view_config
from pyramid.security import Authenticated
from ..security import MyAuthenticationPolicy
from pyramid.httpexceptions import  HTTPFound


@view_config(route_name='welcome', renderer='omegatodo:templates/welcome.mako')
def welcome_view(request):
    if request.authenticated_userid:
        return HTTPFound(location=request.route_url('list'))
    return {}