# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, _


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    user_id = fields.Many2one('res.users', string='Usuario')
