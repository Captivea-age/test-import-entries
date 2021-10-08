# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import api, fields, models


class ImportItem(models.Model):

    _name='account.import.item'

    name = fields.Char(string="Name")
    import_entry_id = fields.Many2one('account.import.entry', string="Import journal entry")
    active = fields.Boolean(string="Active", default="True")
    currency_id = fields.Many2one('res.currency', string="Currency", default="2")
    account_id = fields.Many2one('account.account', string="Account")
    debit = fields.Float(string="Debit")
    credit = fields.Float(string="Credit")
    fully_imported = fields.Boolean(string="Fully imported")
    journal_entry_id = fields.Many2one('account.move', string="Journal entry")
    product_id = fields.Many2one('product.template',string="Product")
    price_unit = fields.Float(string="Unit Price")
    quantity = fields.Float(string="Quantity")
    partner_id = fields.Many2one('res.partner',string="Contact")
