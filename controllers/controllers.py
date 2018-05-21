# -*- coding: utf-8 -*-
from odoo import http

# class PacVenRelated(http.Controller):
#     @http.route('/pac_ven_related/pac_ven_related/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pac_ven_related/pac_ven_related/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pac_ven_related.listing', {
#             'root': '/pac_ven_related/pac_ven_related',
#             'objects': http.request.env['pac_ven_related.pac_ven_related'].search([]),
#         })

#     @http.route('/pac_ven_related/pac_ven_related/objects/<model("pac_ven_related.pac_ven_related"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pac_ven_related.object', {
#             'object': obj
#         })