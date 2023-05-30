#
#     Title: Subject class
#     Author: Felipe Rocha Dias; Gustavo Neves de Paiva
#     Subject: Implementação e Teste de Projeto de Software
#     Teacher: Pedro Toledo
#
from odoo import fields, models, api


class Subject(models.Model):
    _name = 'subject'

    name = fields.Char('Subject Name')
