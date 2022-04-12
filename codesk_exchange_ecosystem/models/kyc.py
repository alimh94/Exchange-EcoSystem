# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError


class ResKyc(models.Model):
    _name = 'res.kyc'

    first_name = fields.Char(string="First Name")
    second_name = fields.Char(string="Second Name")
    third_name = fields.Char(string="Third Name")
    last_name = fields.Char(string="Last Name")
    latin_name = fields.Char(string="Latin Name")

    sequence = fields.Integer(string="Sequence")
    id_type = fields.Selection([('id', 'ID'), ('passport', 'Passport'), ('residency', 'Residency')],
                             string="ID Type", default='id')
    id_issue_date = fields.Date(string="ID Issue Date")
    id_expiry_date = fields.Date(string="ID Expiry Date")
    id_number = fields.Char(string="ID Number")
    country_id = fields.Many2one('res.country', 'Nationality (Country)')
    iso_code = fields.Char(string="ISO Code")
    dob = fields.Date(string="Date of Birth")
    birth_country_id = fields.Many2one('res.country', 'Birth Country')
    birth_state_id = fields.Many2one('res.country.state', string="Birth State",
                                     domain="[('country_id', '=?', country_id)]")
    birth_city = fields.Char('Birth City')
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')
    residency_country_id = fields.Many2one('res.country', 'Residency Country')
    residency_state_id = fields.Many2one('res.country.state', string="Residency State",
                                     domain="[('country_id', '=?', country_id)]")
    residency_city = fields.Char('Residency City')
    street = fields.Char('Street', store=True)
    street2 = fields.Char('Street2', store=True)
    job_id = fields.Many2one('hr.job', 'Job Position')
    doj = fields.Date(string="Date of Join")
    employer_id = fields.Many2one('res.partner', 'Employer')
    employer_phone = fields.Char(string='Employer Phone')
    employer_email = fields.Char(string='Employer Email')
    employer_fax = fields.Char(string='Employer Fax')
    #transaction_type
    monthly_transfer = fields.Integer(string='Monthly Transfer')
    annual_transfer = fields.Integer(string='Annual Transfer')
    average_transfer = fields.Integer(string='Average Transfer')
    annual_limit = fields.Integer(string='Annual Limit')
    #average_transfer_word = fields.Char(string='Average Transfer words')
    #source_of_income
    #purpos
    beneficiary_relation = fields.Selection([
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('sister', 'Sister'),
        ('brother', 'Brother'),
        ('cousin', 'Cousin'),
        ('other', 'Other')
    ], string='Beneficiary Relation')
    pep_relative = fields.Boolean('PEP Relative', default=False, tracking=True)
    pep_relative_relation = fields.Selection([
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('sister', 'Sister'),
        ('brother', 'Brother'),
        ('cousin', 'Cousin'),
        ('other', 'Other')
    ], string='Beneficiary Relation')
    id_front = fields.Binary(string='ID Front')
    id_back = fields.Binary(string='ID Back')