# -*- coding: utf-8 -*-
{
    'name': "pac_ven_related",

    'summary': """
        Packing List No berelasi dengan field Vendor Reference""",

    'description': """
        Modul untuk membuat relasi Packing List No dengan Vendor Reference
    """,

    'author': "Satiya WaraPutra | satiya@energyx.co.id | 087876052503",
    'website': "http://energyx.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
