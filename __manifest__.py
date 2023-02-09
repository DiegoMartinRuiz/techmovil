# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'TechMovil',
    'version': '1.0',
    'category': 'Extras',
    'author': 'Diego Ruiz',
    'depends': [],
    'description': """
Este modulo tiene como objetivo la integracion de toda la informacion necesaria para el seguimiento de las
actividades registradas en los sistemas de CLARO con relacion a TechMovil
    """,
    'data': [
        'views/tech_toa.xml',
        'views/tech_stock_seriados.xml',
        'views/tech_stock_no_seriados.xml',
        'views/tech_principal.xml',
        'views/tech_cuadrillas.xml',
        'security/ir.model.access.csv', 
    ],
 
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'application': True, 
}
