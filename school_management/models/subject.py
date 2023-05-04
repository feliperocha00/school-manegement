from odoo import fields, models, api


class Subject(models.Model):
    _name = 'subject'

    name = fields.Char('Subject Name')
