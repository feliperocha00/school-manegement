from odoo import fields, models, api


class Teacher(models.Model):
    _inherit = 'res.partner'

    subject = fields.Many2one(comodel_name='subject')

    school_id = fields.Many2one(comodel_name='school')