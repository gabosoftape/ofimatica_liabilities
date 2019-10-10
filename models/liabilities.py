# -*- coding: utf-8 -*-
##############################################################################
#
#    Gabosoft Technologies Pvt. Ltd.
#
##############################################################################
from odoo import models, fields, api, _


class LiabilitiesFeatures(models.Model):
    _name = 'liabilities.features'

    name = fields.Char("Nombre")
    cod = fields.Float(string="Codigo")

class LiabilitiesAsambleas(models.Model):
    _name = 'liabilities.asambleas'
    _description = "Asambleas"
    _rec_name = 'nombre'

    doc_count = fields.Integer(string="Numero de documentos", compute='_get_attached_docs')
    nombre = fields.Char('Nombre de la asamblea')

    @api.multi
    def _get_attached_docs(self):
        for record in self:
            domain = [('res_model', '=', self._name), ('res_id', '=', record.id)]
            record.doc_count = self.env['ir.attachment'].search_count(domain)

    @api.multi
    def attachment_tree_view(self):
        domain = [('res_model', '=', self._name), ('res_id', 'in', self.ids)]
        return {
            'name': 'Documentos',
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'kanban,tree,form',
            'view_type': 'form',
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, self.id)
        }