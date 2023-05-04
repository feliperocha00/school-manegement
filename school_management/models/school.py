from odoo import fields, models, api


class School(models.Model):
    _name = 'school'

    name = fields.Char('School Name')

    street = fields.Char('Street')

    city = fields.Char('City')

    district = fields.Char('District')

    state = fields.Char('State')

    zip = fields.Char('Zip Code')

    country = fields.Char('Country')
