# -*- coding: utf-8 -*-
##############################################################################
#
#    Gabosoft Technologies Pvt. Ltd.
#
##############################################################################
from odoo import models, fields, api, _


class PropertyNext(models.Model):
    _name = 'property.liabilities_features'

    name = fields.Char("Nombre")