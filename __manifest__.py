# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Reportes de Ventas',
    'version': '14.0',
    'summary': 'Módulo de perfil de reporte de ventas',
    'sequence': 30,
    'author': 'Versatil SRL.',
    'description': """
        El módulo crea un perfil de usuario y se asocia con el campo 'Sucursales Rep. Ventas' para habilitar al
        usuario un menú nuevo (Reporte de Ventas) en el módulo de Ventas que filtra todas las ventas de las 
        Sucursales asociadas. El usuario no puede editar ni realizar ninguna acción en las ventas del reporte. 
        1. El módulo crea un nuevo perfil 'Reporte de ventas'
        2. Campo "Sucursales Rep. Ventas en formulario de usuario
        3. Manú "Reporte de Ventas" en módulo de Ventas. 
    """,
    'category': 'Ventas',
    'website': 'https://versatil.com.bo',
    'images': [],
    'depends': ['sale', 'base', 'stock', 'vr_corocruz', 'vr_sales_visualization'],
    'data': [
        'security/security_data.xml',
        'security/ir.model.access.csv',
        'views/res_users_view.xml',
        'views/sale_order_view.xml',
        'report/follow_sale_report.xml',
    ],
    'installable': True,
    'auto_install': False,
}