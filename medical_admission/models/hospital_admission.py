from odoo import models, fields, api, _

class HospitalAdmission(models.Model):
    _name = 'hospital.admission'
    _description = 'Hospital Admission'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Admission ID', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, tracking=True)
    
    urgency_level = fields.Selection([
        ('normal', 'Normal'),
        ('urgent', 'Urgent'),
        ('emergency', 'Emergency')
    ], string='Urgency Level', default='normal', required=True, tracking=True)
    
    triage_required = fields.Boolean(compute='_compute_triage_required', store=True)
    triage_notes = fields.Text(string='Triage Notes')
    
    has_social_insurance = fields.Boolean(compute='_compute_has_social_insurance', string='Has Social Insurance', readonly=True)
    social_insurance_id = fields.Many2one('res.partner', related='patient_id.social_insurance_id', string='Insurance Provider', readonly=True)
    
    has_appointment = fields.Boolean(string='Has Appointment', default=False)
    appointment_datetime = fields.Datetime(string='Scheduled Time', tracking=True)
    specialist_id = fields.Many2one('medical.specialty', string='Specialist', tracking=True)
    
    copayment_amount = fields.Monetary(string='Copayment Amount', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('triage', 'Triage'),
        ('admitted', 'Admitted'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', tracking=True)

    @api.depends('patient_id.social_insurance_id')
    def _compute_has_social_insurance(self):
        for record in self:
            record.has_social_insurance = bool(record.patient_id.social_insurance_id)

    @api.depends('urgency_level')
    def _compute_triage_required(self):
        for record in self:
            record.triage_required = record.urgency_level in ['urgent', 'emergency']
            if record.triage_required and record.state == 'draft':
                record.state = 'triage'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                # Try to get the sequence, create it if it doesn't exist
                sequence = self.env['ir.sequence'].sudo().search([('code', '=', 'hospital.admission')], limit=1)
                if not sequence:
                    sequence = self.env['ir.sequence'].sudo().create({
                        'name': 'Hospital Admission Sequence',
                        'code': 'hospital.admission',
                        'prefix': 'ADM/%(year)s/',
                        'padding': 5,
                        'company_id': False,
                    })
                vals['name'] = sequence.next_by_id() or _('New')
        return super(HospitalAdmission, self).create(vals_list)

    def action_admit(self):
        self.state = 'admitted'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancelled'
