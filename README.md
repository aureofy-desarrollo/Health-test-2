# Health-test-2

1. Módulo: Hospital Admission Management (medical_admission)
Este es el módulo base del sistema de salud. Se encarga de la entrada inicial del paciente al centro médico.

Propósito principal: Gestionar el registro de pacientes, admisiones iniciales y la clasificación de urgencias (Triage).

Funcionalidades clave:
Registro de Pacientes: Almacena la información básica y de contacto de las personas.
Gestión de Admisiones: Registro del motivo de la consulta y seguimiento del proceso de entrada.
Triage (Clasificación): Sistema para evaluar la urgencia de los pacientes.
Seguimiento de Seguros y Copagos: Gestión de la cobertura médica y los pagos compartidos.
Modelos principales:
hospital.patient: Datos maestros del paciente.
medical.specialty: Catálogo de especialidades médicas.
hospital.admission: Registro detallado de cada admisión y su clasificación.

2. Módulo: Medical Inpatient Management (medical_inpatient)
Este módulo extiende las capacidades del anterior para gestionar a los pacientes que requieren quedarse internados en el hospital.

Propósito principal: Controlar las hospitalizaciones (internaciones) de larga duración y el equipamiento utilizado.

Funcionalidades clave:

Gestión de Internaciones: Seguimiento del tiempo de estancia, motivos de la internación y estado del paciente.

Integración con Admisiones: Conecta directamente con los pacientes registrados en medical_admission.

Control de Equipamiento Médico: Permite gestionar qué equipos (monitores, respiradores, etc.) se están utilizando durante la internación.

Visibilidad de Seguro Social: Muestra de forma rápida la cobertura del paciente durante su estancia.
Modelos principales:
medical.inpatient: El registro central de la hospitalización.
medical.equipment: Catálogo y estado de los equipos médicos.
hospital.patient (extensión): Añade campos específicos relacionados con la internación.

Resumen de la Arquitectura
Dependencia: El módulo de Inpatient depende directamente del de Admission. No puedes tener la gestión de internaciones sin el sistema base de registro y admisión de pacientes.
Enfoque: Ambos módulos están diseñados siguiendo las mejores prácticas de Odoo (versión 17/18 según la estructura), utilizando manifiestos claros y una separación limpia entre modelos, vistas y seguridad.

