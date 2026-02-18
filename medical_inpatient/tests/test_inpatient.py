from odoo.tests.common import TransactionCase

class TestMedicalInpatient(TransactionCase):

    def test_basic_inpatient_creation(self):
        """A simple test to satisfy the Odoo test runner and silence the '0 tests' warning."""
        patient = self.env['hospital.patient'].create({
            'name': 'Test Inpatient',
            'id_number': '87654321'
        })
        registration = self.env['medical.inpatient.registration'].create({
            'patient_id': patient.id,
            'reason': 'Test Reason'
        })
        self.assertEqual(registration.state, 'draft', "Initial state should be draft")
