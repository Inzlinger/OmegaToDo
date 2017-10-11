import os
from pyramid.security import Allow, Everyone, Authenticated

here = os.path.dirname(os.path.abspath(__file__))

class Public(object):
    __acl__ = [(Allow, Everyone, 'view')]
 
    def __init__(self, request):
        pass

class AuthenticationRequired(object):
    __acl__ = [(Allow, Authenticated, 'view')]

    def __init__(self, request):
        pass

def includeme(config):
    config.add_static_view('static', path=os.path.join(here, 'static'))

    config.add_route('welcome','/', factory=Public)
    config.add_route('list', '/list/', factory=AuthenticationRequired)
    config.add_route('new', '/new', factory=AuthenticationRequired)
    config.add_route('close', '/close/{id}', factory=AuthenticationRequired)
    config.add_route('open', '/open/{id}', factory=AuthenticationRequired)
    config.add_route('edit', '/edit/{id}' , factory=AuthenticationRequired)
    config.add_route('delete', '/delete/{id}', factory=AuthenticationRequired)
    config.add_route('savededit', '/savededit/{id}', factory=AuthenticationRequired)
    config.add_route('login', '/login', factory=Public)
    config.add_route('logout', '/logout', factory=AuthenticationRequired)
    config.add_route('signin', '/signin', factory=Public)

    config.add_route('updatepriority', '/updatepriority', factory=AuthenticationRequired)