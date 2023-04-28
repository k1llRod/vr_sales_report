# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools
from odoo.exceptions import UserError


class FollowSaleReport(models.Model):
    _name = "follow.sale.report"
    _description = 'Reporte Seguidor Ventas'
    _auto = False
    _order = 'sale_id asc'

    sale_id = fields.Integer("ID Orden de Venta")
    name = fields.Char("Número")
    state = fields.Selection([
        ('draft', 'Cotización'),
        ('sent', 'Cotización Enviada'),
        ('sale', 'Pedido de Venta'),
        ('done', 'Bloqueado'),
        ('cancel', 'Cancelado'),
    ], string='Estado')
    invoice_status = fields.Selection([
        ('upselling', 'Oportunidad de Venta'),
        ('invoiced', 'Facturado'),
        ('to invoice', 'A facturar'),
        ('no', 'Nada por facturar')
    ], string='Estado de Factura')
    date_order = fields.Datetime(string='Fecha de Venta')
    user_id = fields.Many2one('res.users', 'Vendedor')
    employee_id = fields.Many2one('hr.employee', 'Empleado')
    partner_id = fields.Many2one('res.partner', 'Cliente')
    nit_ci = fields.Char('NIt/CI')
    warehouse_id = fields.Many2one('stock.warehouse', 'Sucursal')
    amount_total = fields.Float('Monto Total de Venta')

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'follow_sale_report')
        query = """
            CREATE OR REPLACE VIEW follow_sale_report AS (
            select 
                row_number() over() as id,	
                id sale_id,
                name,
                state,
                invoice_status,
                date_order,
                user_id,
                employee_id,
                partner_id,
                nit_ci,
                warehouse_id,
                amount_total
            from sale_order so
            )
            """
        self.env.cr.execute(query)

    def action_view_sale(self):
        for r in self:
            return {
                    'name': 'Venta',
                    'res_id': r.sale_id,
                    'res_model': 'sale.order',
                    'type': 'ir.actions.act_window',
                    'view_id': False,
                    'view_mode': 'form',
                    'view_type': 'form',
                    'context': {
                        'create': False,
                        'edit': False,
                        'visibility_report': True,
                    },
                }

    def _get_report(self):
        warehouses = self.env.user.warehouse_ids and self.env.user.warehouse_ids.ids or False
        return {
            'name': 'Reporte Seguimiento de Ventas',
            'res_model': 'follow.sale.report',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree',
            'view_type': 'form',
            'domain': [('warehouse_id', 'in', warehouses or False)],
        }