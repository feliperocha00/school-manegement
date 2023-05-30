#
#     Title: Teacher class
#     Author: Felipe Rocha Dias; Gustavo Neves de Paiva
#     Subject: Implementação e Teste de Projeto de Software
#     Teacher: Pedro Toledo
#
from odoo import fields, models, api


class Teacher(models.Model):
    # _inherits = {'res.partner': 'name'}
    _name = 'teacher'

    subject = fields.Many2one(comodel_name='subject')

    school_id = fields.Many2one(comodel_name='school')
