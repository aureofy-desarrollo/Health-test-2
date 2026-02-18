from odoo import models, fields, api

class HospitalPatient(models.Model):
    _inherit = 'hospital.patient'

    registration_ids = fields.One2many(
        'medical.inpatient.registration', 'patient_id',
        string='Inpatient Registrations'
    )

    is_hospitalized = fields.Boolean(
        string='Is Hospitalized',
        compute='_compute_is_hospitalized',
        store=True,
        help="Checks if the patient is currently hospitalized"
    )

    @api.depends('registration_ids.state')
    def _compute_is_hospitalized(self):
        for record in self:
            record.is_hospitalized = any(reg.state == 'hospitalized' for reg in record.registration_ids)
