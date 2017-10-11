from pyramid.view import view_config
from pyramid.security import Authenticated, authenticated_userid
from pyramid.httpexceptions import  HTTPFound, HTTPForbidden
import re
import transaction
import datetime

from ..models.task import Task
from ..security import MyAuthenticationPolicy



@view_config(route_name='new', renderer='omegatodo:templates/new.mako', permission='view')
def new_view(request):
    if request.method == 'POST':
        if request.POST.get('name'): 
            dateString = request.POST['date']
            regexDate = re.compile(r'\b\d{4}-\d\d?-\d\d?\b')
            if (regexDate.search(dateString))is not None:
                dateStrings = dateString.split("-", 3)
                date = datetime.date(int(dateStrings[0]), int(dateStrings[1]), int(dateStrings[2]))
                user = request.authenticated_userid
                newTask = Task(text=request.POST.get('name'), due = date, owner = user)

                request.dbsession.add(newTask)
                transaction.commit()
                request.session.flash('Neuer Eintrag erfolgreich eingefügt!')
                return HTTPFound(location=request.route_url('list', userid=user))
            else:
                request.session.flash('Invalides Datumsformat!')         
        else:
            request.session.flash('Bitte geben Sie einen Namen ein!')
    return {}