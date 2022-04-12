# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError


class ShiftTransaction(models.Model):
    _name = 'shift.transaction'
    _description = 'Financial Transactions'

    first_currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    second_currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    transaction_type= fields.Selection([('sell', 'Sell'), ('buy', 'Buy'), ('exchange','Exchange')],
                                       string="Type", store=True, default='open')
    state = fields.Selection([('pending_approval', 'Pending Approval'), ('approved', 'Approved')],
                             string="State", store=True, default='pending_approval')
    amount = fields.Float(string='amount', required=True)
    fee = fields.Float(string='Fee')
    shift_id = fields.Many2one('shift', string='Shift', required=True)
    customer_id = fields.Many2one('res.partner', 'Customer')