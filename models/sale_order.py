# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, _, api
from odoo.addons.base.models import res_users


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _get_action(self, xml_id):
        action = self.env['ir.actions.act_window']._for_xml_id(xml_id)
        user = self.env.user
        domain = []
        if xml_id == 'sale.action_orders':
            domain.append(('state', 'not in', ('draft', 'sent', 'cancel')))
        if user.has_group('sales_team.group_sale_salesman_all_leads'):
            a = 10
        elif user.has_group('sales_team.group_sale_salesman'):
            domain.append(('user_id', '=', user.id))
        action['domain'] = domain
        return action

    def _init_remake(self):
        action = super(SaleOrder, self)._init_remake()
        user = self.env.user
        domain = action['domain']
        if user.has_group('sales_team.group_sale_salesman_all_leads'):
            a = 10
        elif user.has_group('sales_team.group_sale_salesman'):
            domain.append(('user_id', '=', user.id))
        action['domain'] = domain
        return action

