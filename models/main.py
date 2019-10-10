# -*- coding: utf-8 -*-
##############################################################################
#
#    Gabosoft Technologies Pvt. Ltd.
#
##############################################################################

from datetime import datetime, date, timedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning


class propertyNext(models.Model):
    _name='property.liabilities.features'

    name=fields.Char("Nombre")
