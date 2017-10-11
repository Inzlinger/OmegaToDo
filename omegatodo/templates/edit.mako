# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>Eintrag Bearbeiten</h1>
<% user = request.authenticated_userid %>
<% task_id = int(request.matchdict['id']) %>

<form action="${request.route_url('savededit',id =task_id )}" method="post">
    <input type="text" maxlength="100" name="name", value="${zustand[0]}">
    <input type="date" name="date", value="${zustand[1]}">
    <input type="submit" name="add" value="Speichern" class="button">
</form>
