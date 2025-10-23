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
        "security/ir.model.access.csv",
        "security/hr_employee_security.xml",
        "views/hr_employee.xml",
        "views/hr_employee_public.xml",
        "views/hr_employee_certification.xml",
    ],
    "installable": True,
    "application": False,
}
