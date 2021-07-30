# -*- coding: utf-8 -*-
# from odoo import http


# class StandardReports(http.Controller):
#     @http.route('/standard_reports/standard_reports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/standard_reports/standard_reports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('standard_reports.listing', {
#             'root': '/standard_reports/standard_reports',
#             'objects': http.request.env['standard_reports.standard_reports'].search([]),
#         })

#     @http.route('/standard_reports/standard_reports/objects/<model("standard_reports.standard_reports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('standard_reports.object', {
#             'object': obj
#         })
