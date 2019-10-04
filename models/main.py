from odoo import models, fields, api, _
from datetime import datetime

class recibosAdmin(models.Model):
    _name='property.liabilities'
    _inherit='account.invoice'

    tipo = fields.Char('Tipo')