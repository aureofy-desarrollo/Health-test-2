from odoo.tests.common import TransactionCase

class TestHospitalAdmission(TransactionCase):

    def test_basic_admission_creation(self):
        """A simple test to satisfy the Odoo test runner and silence the '0 tests' warning."""
        patient = self.env['hospital.patient'].create({
            'name': 'Test Patient',
            'id_number': '12345678'
        })
        admission = self.env['hospital.admission'].create({
            'patient_id': patient.id,
            'urgency_level': 'normal'
        })
        self.assertEqual(admission.state, 'draft', "Initial state should be draft")
