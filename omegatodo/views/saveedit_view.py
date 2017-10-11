from pyramid.view import view_config
from pyramid.security import Authenticated
from pyramid.httpexceptions import HTTPFound
import re
import transaction
import datetime

from ..models.task import Task

@view_config(route_name='savededit', permission='view')
def savededit_view(request):
    task_id = int(request.matchdict['id'])
    if request.method == 'POST':
        if request.POST.get('name'):
            dateString = request.POST['date']
            regexDate = re.compile(r'\b\d{4}-\d\d?-\d\d?\b')
            if (regexDate.search(dateString))is not None:
                dateStrings = dateString.split("-", 3)
                task = request.dbsession.query(Task).filter_by(id=task_id).first()
                task.text = request.POST['name']
                task.due = datetime.date(int(dateStrings[0]), int(dateStrings[1]), int(dateStrings[2]))
                transaction.commit()
                request.session.flash('Eintrag erfolgreich bearbeitet!')
                return HTTPFound(location=request.route_url('list'))
            else:
                request.session.flash('Invalides Datumsformat!')
        else:
            request.session.flash('Bitte geben Sie einen Namen ein!')
    return HTTPFound(location=request.route_url('edit', id=task_id))