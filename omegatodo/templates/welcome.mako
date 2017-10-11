# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>OmegaToDo</h1>
<form action="${request.route_url('login')}" method="post">
    <input type="submit" name="add" value="Login" class="button">
</form><form action="${request.route_url('signin')}" method="post">
    <input type="submit" name="add" value="Nutzer Erstellen" class="button">
</form><form action="${request.route_url('logout')}" method="post">
    <input type="submit" name="add" value="Logout" class="button">
</form>