# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'academy.course'
    _description = 'Academy Course Description'
    _rec_name = 'title'

    title = fields.Char(string='Course Title', Required=True)
    description = fields.Text(string='Course Description')
    responsible_user_id = fields.Many2one('res.users', string='Responsible User')
    session_ids = fields.One2many('academy.session', 'course_id', string='Course Sessions')


class Session(models.Model):
    _name = 'academy.session'
    _description = 'Academy Course Session'
    _rec_name = 'name'

    name = fields.Char(string='Session Name')
    start_date = fields.Date(string='Start Date')
    duration = fields.Integer(string='Session Duration')
    number_seats = fields.Integer(string='Number of seats')
    instructor_id = fields.Many2one('res.partner', string='Instructor')
    course_id = fields.Many2one('academy.course', string='Related Course', required=True)
    attendees = fields.Many2many('res.partner', string='Attendees')


class NewPartner(models.Model):
    _name = 'academy.partner'
    _description = 'Academy Partner'
    _inherit = 'res.partner'

    instructor = fields.Boolean(string='Is an Instructor?', default=False)
    sessions_ids = fields.Many2many('academy.session', string='Partner Sessions')

    @api.model
    def write(self, values):
        if values.get('duration') == 0:
            values['number_seats'] = 100
        return super(Session, self).write(values)
    @api.model
    def create(self, values):
        # Add code here
        return super(ClassName, self).create(values)

