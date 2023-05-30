#
#     Title: Classes class
#     Author: Felipe Rocha Dias; Gustavo Neves de Paiva
#     Subject: Implementação e Teste de Projeto de Software
#     Teacher: Pedro Toledo
#
from odoo import fields, models, api


class Classes(models.Model):
    _name = 'classes'
    _rec_name = 'class_num'

    class_num = fields.Char()

    teacher_id = fields.Many2many(comodel_name='res.users')