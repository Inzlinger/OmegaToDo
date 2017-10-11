import bcrypt
from pyramid.httpexceptions import  HTTPFound
from pyramid.view import view_config
from pyramid.security import Authenticated
from pyramid.security import remember
from ..models import User

@view_config(route_name='login', renderer='omegatodo:templates/login.mako', permission='view')
def login(request):
    if request.method == 'POST':
        if request.POST.get('name'): 
            login = request.POST['name']
            if request.POST.get('password'):
                pw = request.POST['password']
                user = request.dbsession.query(User).filter_by(name=login)
                if user.first():
                    username = user.first().name
                    if user.first().check_password(pw):
                        headers = remember(request, user.first().id)
                        request.session.flash('Login erfolgreich!')
                        return HTTPFound(location=request.route_url('welcome'), headers=headers)
                    else: 
                        request.session.flash('Falsches Passwort!')
                else: 
                    request.session.flash('Nutzer existiert nicht!')    
                request.session.flash('Login Fehlgeschlagen!')
            else:
                request.session.flash('Bitte geben Sie ein Passwort ein!')
        else:
            request.session.flash('Bitte geben Sie einen Namen ein!')
    return {}