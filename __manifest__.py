# -*- coding: utf-8 -*-
# ©  2015-2019 Ofimatica Soluciones
#              Gabriel Pabon<gabosoft.ape(@)gmail(.)com
# See README.rst file on addons root folder for license details

{
    "name": "Obligaciones Ofimatica",
    'version': '12.0.1.1.0',
    "author": "Gabriel Pabón",
    "website": "https://www.ofimaticasoluciones.com.co",

    "category": "Property",
    "depends": [
        'account',
        'board',
    ],
    "license": "LGPL-3",
    "data": [
        'security/ofimatica_liabilities_security.xml',
        'views/account_invoice.xml',
        'views/menus.xml',


    ],
    'application': False,
    "images": ['images/main_screenshot.png'],
    "installable": True,
}