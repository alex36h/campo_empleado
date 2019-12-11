# -*- coding: utf-8 -*-
from odoo import http

# class CampoEmpleado(http.Controller):
#     @http.route('/campo_empleado/campo_empleado/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/campo_empleado/campo_empleado/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('campo_empleado.listing', {
#             'root': '/campo_empleado/campo_empleado',
#             'objects': http.request.env['campo_empleado.campo_empleado'].search([]),
#         })

#     @http.route('/campo_empleado/campo_empleado/objects/<model("campo_empleado.campo_empleado"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('campo_empleado.object', {
#             'object': obj
#         })