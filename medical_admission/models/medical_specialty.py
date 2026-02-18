from odoo import models, fields

class MedicalSpecialty(models.Model):
    _name = 'medical.specialty'
    _description = 'Medical Specialty'
    _order = 'name'

    name = fields.Char(string='Specialty Name', required=True, translate=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(default=True)
