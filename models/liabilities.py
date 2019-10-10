# -*- coding: utf-8 -*-
##############################################################################
#
#    Gabosoft Technologies Pvt. Ltd.
#
##############################################################################
from odoo import models, fields, api, _


class PropertyNext(models.Model):
    _name = 'liabilities.features'

    name = fields.Char("Nombre")
    cod = fields.Float(string="Codigo")