{
    "name": "HR YHC Employee",
    "version": "1.0.0",
    "summary": "Yayasan Hasnur Center Employee Management",
    "category": "Human Resources",
    "author": "Muhammad Sohiburroihan Akbar",
    "depends": [
        "hr",
        "hr_skills_survey",
    ],
    "data": [
        "security/hr_area_groups.xml",
        "security/office_groups.xml",
        "security/hr_employee_security.xml",
        "security/hr_resume_rules.xml",
        "security/ir.model.access.csv",
        "views/hr_employee.xml",
        "views/hr_employee_public.xml",
        "views/hr_employee_certification.xml",
        'views/hr_training_certificate.xml',
    ],
    "installable": True,
    "application": False,
}
