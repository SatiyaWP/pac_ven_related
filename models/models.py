# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class pac_ven_related(models.Model):
#     _name = 'pac_ven_related.pac_ven_related'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class venpack(models.Model):
    _inherit = 'purchase.order'

    packing_list_no = fields.Char(related= 'partner_ref', readonly=True, required=False)
