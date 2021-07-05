# -*- coding: utf-8 -*-
{
    'name': "Vauxoo Javascript Webinar",
    'summary': "Vauxoo Javascript Webinar for Odoo 13",
    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create and use
        JavaScript functionalities in Odoo 13.

        Source: https://www.youtube.com/c/Vauxoo/search?query=odoo%20javascript
    """,
    'version': '13.0.1.0.0',
    'author': 'Vauxoo',
    'website': 'https://www.vauxoo.com/',
    'support': 'info@vauxoo.com',
    'maintainer': 'Leonardo J. Caballero G. <leonardocaballero@gmail.com>',
    'license': 'AGPL-3',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorial',
    # Any module necessary for this one to work correctly
    'depends': [
        'base',
        'web',
        'website',
        'product',
        'website_sale'
    ],
    # Always loaded
    'data': [
        'views/assets.xml',
        'views/products.xml'
    ],
    # Only loaded in demonstration mode
    'demo': [],
    # QWeb templates
    'qweb': [],
    'images': [
        'static/description/icon.png'
    ],
    'installable': True,
    'application': True,
}

