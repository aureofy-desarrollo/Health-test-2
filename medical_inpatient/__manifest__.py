{
    'name': 'Medical Inpatient Management',
    'version': '1.0',
    'category': 'Medical',
    'summary': 'Manage patient hospitalizations and equipment',
    'description': """
        This module allows managing patient hospitalizations (internación).
        - Connects with patients from medical_admission.
        - Tracks hospitalization time and reason.
        - Displays patient's social insurance.
        - Manages equipment usage during hospitalization.
    """,
    'author': 'Antigravity',
    'depends': ['base', 'medical_admission'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/medical_equipment_views.xml',
        'views/medical_inpatient_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [
        'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
