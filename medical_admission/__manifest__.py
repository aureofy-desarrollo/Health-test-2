{
    'name': 'Hospital Admission Management',
    'version': '1.0',
    'category': 'Medical',
    'summary': 'Manage patient admissions, triage, and copayments',
    'description': """
        This module provides functionality for:
        - Patient registration
        - Admission management
        - Urgency and Triage assessment
        - Insurance and Copayment tracking
    """,
    'author': 'Antigravity',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_patient_views.xml',
        'views/medical_specialty_views.xml',
        'views/hospital_admission_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [
        'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
