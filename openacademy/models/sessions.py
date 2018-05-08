from odoo import api, fields, models

class Sessions(models.Model):
    _name = 'openacademy.sessions'
    _rec_name = 'name'  #ceci est afin de montrer un titre par default, sinon on vois seulement une entree de donné

    name = fields.Char(string='Course Name')
    start_date = fields.Date(default=fields.Date.today, string='Start Date')
    duration = fields.Integer(string='Duration')
    nbr_oS = fields.Integer(string='Number of Sessions')
    rel_courses = fields.Many2one(comodel_name="openacademy.course", string='Related courses', required='true')
    instructor = fields.Many2one(comodel_name="res.partner", string="Related Instructor", required='true')

    course_id = fields.Many2one(comodel_name='course', ondelete="set null", string="Related course:", required="True")
    instructor_id = fields.Many2one(comodel_name='res.partner', ondelete="set null", string="Instructor:")
    responsible_id = fields.Many2one(comodel_name='res.users', ondelete="set null", string="Responsible:")

    attendees = fields.Many2many(comodel_name="res.partner", relation="session_attendees", column1="session_id", column2="attendee_id")