from odoo import models, fields

class MedicalEquipment(models.Model):
    _name = 'medical.equipment'
    _description = 'Medical Equipment'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
