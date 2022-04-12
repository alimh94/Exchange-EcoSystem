# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError


class Shift(models.Model):
    _name = 'shift'
    _description = 'Teller daily Shift'
    name = fields.Char(string='Shift Name', translate=True, store=True, readonly=True, compute="_get_shift_name")\

    @api.depends('create_date')
    def _get_shift_name(self):
        self.name = self.env.user.name + '_' + str(self.create_date)[:10]

    user_id = fields.Many2one('res.users', string='User', ondelete='cascade', readonly=True, default=lambda self: self.env.user)

    closing_date = fields.Datetime(string='Closing Date', readonly=True)

    # branch_id = fields.Many2one('res.branch', string='Branch')
    # account_move_ids = fields.One2many('account.move', string='Transactions')
    transaction_ids = fields.One2many('shift.transaction', 'shift_id', string='Transactions')
    shift_line_ids = fields.One2many('shift.line', 'shift_id', string='Shift Lines')
    state = fields.Selection([('open', 'Open'), ('confirmed_open','Confirmed Open'), ('closed', 'Closed'),
                               ('confirmed_closed', 'Confirmed closed')], string="State", store=True, default='open')

    @api.depends('state', 'create_uid')
    def _check_open_shifts(self):
        user_ids = self.mapped("create_uid")
        for user in user_ids:
            open_shifts = self.search([("state", "=", "open"), ("create_uid", "=", user.id)])
            if len(open_shifts) > 1:
                raise UserError("Only a single open shift is allowed per user")

    def action_confirm_opening(self):
        return self.write({'state': 'confirmed_open'})

    def action_confirm_closing(self):
        return self.write({'state': 'confirmed_closed'})

    def action_close(self):
        return self.write({'state': 'closed'})


class ShiftLine(models.Model):
    _name = 'shift.line'
    _description = 'Teller daily Shift Lines'

    currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    opening_balance = fields.Float(string='Opening Balance', required=True)
    current_balance = fields.Float(string='Current Balance')
    closing_balance = fields.Float(string='Closing Balance')
    shift_id = fields.Many2one('shift', string='Shift', required=True)

