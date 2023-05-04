from odoo import fields, models, api


class Student(models.Model):
    _name = 'student'

    name = fields.Char('School Name')

    age = fields.Integer('Age')

    street = fields.Char('Street')

    city = fields.Char('City')

    district = fields.Char('District')

    state = fields.Char('State')

    zip = fields.Char('Zip Code')

    country = fields.Char('Country')

    school_id = fields.Many2one(comodel_name='school', string='School')

    class_id = fields.Many2one(comodel_name='class', string='Class')

    def register(self):
