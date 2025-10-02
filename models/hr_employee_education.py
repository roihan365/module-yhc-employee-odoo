from odoo import models, fields

class HrEmployeeEducation(models.Model):
    _name = "hr.employee.education"
    _description = "Data Pendidikan Karyawan"

    employee_id = fields.Many2one("hr.employee", string="Karyawan", ondelete="cascade", required=True)

    certificate = fields.Selection([
        ('sd', 'SD'),
        ('smp', 'SMP'),
        ('sma', 'SMA/SMK'),
        ('d1', 'Diploma 1'),
        ('d3', 'Diploma 3'),
        ('s1', 'Sarjana'),
        ('s2', 'Magister'),
        ('s3', 'Doktor')
    ], string="Pendidikan Terakhir")

    faculty = fields.Char(string="Fakultas")
    major = fields.Char(string="Program Studi")
    study_school = fields.Char(string="Nama Sekolah/Universitas")
    year_start = fields.Date(string="Tahun Mulai")
    year_end = fields.Date(string="Tahun Selesai")
    ijazah_number = fields.Char(string="No. Ijazah")
