# -*- coding: utf-8 -*-
{
    "name": "Journal entries import",
    "version": "0.1",
    'author': "Andrew LAW x Abdessamad GERARD",
    'website': "www.captivea.us",
    "category": "Accounting",
    "description": "Allows to import journal entries better than odoo does it",
    "depends": [
        "base","account"
    ],
    "data": [
        "security/ir.model.access.csv",
        'data/server_action.xml',
        'views/views.xml',
    ],
}
