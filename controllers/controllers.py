# -*- coding: utf-8 -*-
from openerp import http

# class VcmsDemo(http.Controller):
#     @http.route('/vcms_demo/vcms_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vcms_demo/vcms_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vcms_demo.listing', {
#             'root': '/vcms_demo/vcms_demo',
#             'objects': http.request.env['vcms_demo.vcms_demo'].search([]),
#         })

#     @http.route('/vcms_demo/vcms_demo/objects/<model("vcms_demo.vcms_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vcms_demo.object', {
#             'object': obj
#         })