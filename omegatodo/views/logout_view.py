from pyramid.view import view_config
from pyramid.security import Authenticated, forget
from pyramid.httpexceptions import  HTTPFound

@view_config(route_name='logout', permission='view')
def logout(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('welcome'), headers=headers)