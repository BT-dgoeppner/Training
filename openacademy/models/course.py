from odoo import api, fields, models

class Course(models.Model):
    _name = 'openacademy.course'
    _rec_name = 'title'  #ceci est afin de montrer un titre par default, sinon on vois seulement une entree de donné

    title = fields.Char(string='Subject')
    date = fields.Date(string='Date')
    description = fields.Text(string='Description')
    responsible = fields.Many2one(comodel_name="res.users", string="Responsible")
    sessions = fields.One2many(comodel_name="sessions.name", string="Sessions_id")

    #sessions = fields.One2many(comodel_name='session', inverse_name="course_id", ondelete="set null", string="Sessions:")
