# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, _
from odoo.addons.base.models import res_users


class ResUsers(models.Model):
    _inherit = 'res.users'

    # warehouse_ids = fields.One2many('stock.warehouse', 'user_id', string='Sucursales Rep. Ventas')
    warehouse_ids = fields.Many2many('stock.warehouse', 'user_warehouse_rel', 'res_user_id', 'warehouse_id', string='Sucursales Rep. Ventas')