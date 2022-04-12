# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Exchange EcoSystem',
    'version' : '1.1',
    'summary': 'Sell, Buy & Echange Currency',
    'description': """ """,
    'category': 'Accounting/Accounting',
    'website': 'https://codesksolutions.co',
    'depends' : ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_currency.xml',
        'views/shift.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
