from pyramid.view import view_config
from sqlalchemy import and_
from ..models import Task, User
from babel.dates import format_date, format_datetime, format_time



@view_config(route_name='list', renderer='omegatodo:templates/list.mako', permission='view')
def list_view(request):
    user = request.authenticated_userid
    name = request.dbsession.query(User).filter_by(id=user).first().id
    username = request.dbsession.query(User).filter_by(id=user).first().name

    activeTasks = request.dbsession.query(Task).filter_by(status=False, owner=name).order_by(Task.priority)
    doneTasks = request.dbsession.query(Task).filter_by(status=True, owner=name).order_by(Task.priority)

    tasksA = [dict(id=row.id, name=row.text, due=format_date(row.due,locale='de_DE'), style=row.get_status_color()) for row in activeTasks.all()]
    tasksD = [dict(id=row.id, name=row.text, due=format_date(row.due,locale='de_DE') , style=row.get_status_color()) for row in doneTasks.all()]

    return {'tasks': (tasksA, tasksD, username)}
