# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import api, fields, models


class ImportEntry(models.Model):

    _name='account.import.entry'

    name = fields.Char(string="Name")
    date = fields.Date(string="Date")
    due_date = fields.Date(string="Due Date")
    journal_id = fields.Many2one('account.journal',string="Journal")
    journal_item_ids = fields.One2many('account.import.item','import_entry_id',string="Journal item import")
    contact_id = fields.Many2one('res.partner',string="Contact")
    sequence = fields.Integer(string="Sequence")
    transferred = fields.Boolean(string="Transferred")
    ref  = fields.Char(string="Ref")
    active = fields.Boolean(string="Active", default="True")
