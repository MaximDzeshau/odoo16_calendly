# -*- coding: utf-8 -*-
from odoo import http

class Calendly(http.Controller):

    @http.route('/calendly/events', auth='public', website=True)
    def index(self, **kw):
        Events = http.request.env['calendar.event']
        return http.request.render('calendly.index', {
            'events': Events.search([])
        })
    
    # @http.route('/academy/<model("academy.teachers"):teacher>/', auth='public', website=True)
    # def teacher(self, teacher):
    #     return http.request.render('academy.biography', {
    #         'person': teacher
    #     })