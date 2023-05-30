#
#     Title: School class
#     Author: Felipe Rocha Dias; Gustavo Neves de Paiva
#     Subject: Implementação e Teste de Projeto de Software
#     Teacher: Pedro Toledo
#
from odoo import fields, models, api


class School(models.Model):
    _name = 'school'

    name = fields.Char('School Name')

    # School address
    street = fields.Char('Street')

    city = fields.Char('City')

    district = fields.Char('District')

    state = fields.Char('State')

    zip = fields.Char('Zip Code')

    country = fields.Char('Country')
