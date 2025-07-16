# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO Open Source Management Solution
#
#    ODOO Addon module by Uncanny Consulting Services LLP
#    Copyright (C) 2023 Uncanny Consulting Services LLP (<https://uncannycs.com>).
#
##############################################################################
{
    "name": "Import Sales Order",
    "website": "https://uncannycs.com",
    "author": "Uncanny Consulting Services LLP",
    "maintainers": "Uncanny Consulting Services LLP",
    "license": "Other proprietary",
    "category": "Extra Tools",
    "summary": "Import Sale Order from excel",
    "description": """This module is useful to import data from CSV/excel file.""",
    "version": "16.0.1.0.0",
    "depends": [
        "sale_management",
    ],
    "data": [
        "security/import_sale_order_security.xml",
        "security/ir.model.access.csv",
        "wizard/import_sale_order_wizard_views.xml",
        "wizard/popup_message_wizard.xml",
        "views/sale_views.xml",
    ],
    "external_dependencies": {
        "python": ["xlrd"],
    },
    "application": False,
    "installable": True,
    "auto_install": False,
    "images": ["static/description/banner.gif"],
    'icon': 'import_sale_order_ucs/static/description/icon.gif',
    "price": 20,
    "currency": "USD",
}
