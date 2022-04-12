# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError


class ResCurrency(models.Model):
    _inherit = 'res.currency'

    tolerance = fields.Float(string='Tolerance', digits=0)


class ResCurrencyRate(models.Model):
    _inherit = "res.currency.rate"

    foreign_sale_price = fields.Float(digits=0,string='Foreign Sale Price')
    foreign_buy_price = fields.Float(digits=0,string='Foreign Buy Price')
    base_sale_price = fields.Float(digits=0,string='Base Sale Price')
    base_buy_price = fields.Float(digits=0,string='Base Buy Price')
    evaluation = fields.Float(digits=0,string='Evaluation')