# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>
<% user = request.authenticated_userid %>

<script type="text/javascript" src="../static/jquery-3.2.1.js"></script>
<script type="text/javascript" src="../static/jquery-ui-1.12.1.custom/jquery-ui.js"></script>

<script type="text/javascript" src="../static/draggableLists.js"></script>


<h1>OmegaToDo</h1>

<h3>Willkommen, ${tasks[2]} [<a href="${request.route_url('logout')}">Logout</a>]</h3> 


<ul id="all">
% if tasks[0]:
 <li class="divider", id="activeheader">Aktive Aufgaben</li>
 <ul id="active">
  % for task in tasks[0]: 
  <li id="${task['id']}")>
    <span class=${task['style']}> <div align = left>${task['name']} ${task['due']}</div> <div align=right>
    [<a href="${request.route_url('edit', id=task['id'])}">bearbeiten</a>]
    [<a href="${request.route_url('close', id=task['id'])}">erledigt</a>]
    [<a href="${request.route_url('delete', id=task['id'])}">löschen</a>]  
    </div>
  </span>
  </li>
  % endfor
  </ul>
% else:
  <li>Es sind keine Aktiven Aufgaben vorhanden!</li>
% endif
% if tasks[1]:
  <li>Erledigte Aufgaben:</li>
  <ul id="done">
  % for task in tasks[1]:
  <li id=${task['id']}>
    <span class="green"}> <div align = left>${task['name']} ${task['due']}  </div> 
    <div align=right>
    [<a href="${request.route_url('edit', id=task['id'])}">bearbeiten</a>]
    [<a href="${request.route_url('open', id=task['id'])}">Aktivieren</a>] 
    [<a href="${request.route_url('delete', id=task['id'])}">löschen</a>]   
    </div>
  </span>
  </li>
  % endfor
% else:
  <li>Es sind keine Erledigten Aufgaben vorhanden!</li>
% endif
</ul>
<ul id="new", class="tasks">
  <li class="last">
    <a href="${request.route_url('new')}">Neuen Eintrag einfügen</a>
  </li>
</ul>


