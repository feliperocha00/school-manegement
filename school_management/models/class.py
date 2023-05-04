from odoo import fields, models, api


class Class(models.Model):
    _name = 'class'
    _rec_name = 'class_num'

    class_num = fields.Char()

    teacher_id = fields.Many2many(comodel_name='res.users')