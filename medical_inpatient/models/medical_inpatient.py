from odoo import models, fields, api, _

class MedicalInpatientRegistration(models.Model):
    _name = 'medical.inpatient.registration'
    _description = 'Inpatient Registration'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Registration ID', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, tracking=True)
    social_insurance_id = fields.Many2one('res.partner', related='patient_id.social_insurance_id', string='Social Insurance', readonly=True, store=True)
    
    start_date = fields.Datetime(string='Start Date', required=True, default=fields.Datetime.now, tracking=True)
    end_date = fields.Datetime(string='End Date', tracking=True)
    reason = fields.Text(string='Reason for Hospitalization', required=True)
    
    equipment_ids = fields.Many2many('medical.equipment', string='Equipment Used')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('hospitalized', 'Hospitalized'),
        ('discharged', 'Discharged'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('medical.inpatient.registration') or _('New')
        return super(MedicalInpatientRegistration, self).create(vals_list)

    def action_hospitalize(self):
        self.state = 'hospitalized'

    def action_discharge(self):
        self.state = 'discharged'
        self.end_date = fields.Datetime.now()
    
    def action_cancel(self):
        self.state = 'cancelled'
