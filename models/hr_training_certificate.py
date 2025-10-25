from odoo import models, fields

class HrTrainingCertificate(models.Model):
    _name = 'hr.training.certificate'
    _description = 'Sertifikat Pelatihan Karyawan'

    employee_id = fields.Many2one('hr.employee', string='Karyawan', ondelete='cascade')
    name = fields.Char(string='Nama Pelatihan', required=True)
    tujuan = fields.Text(string='Tujuan Pelatihan', store=True)
    jenis_pelatihan = fields.Selection([
        ('internal', 'Internal'),
        ('eksternal', 'Eksternal'),
        ('teknis', 'Teknis'),
        ('nonteknis', 'Nonteknis'),
    ], string='Jenis Pelatihan', store=True)
    department_id = fields.Many2one('hr.department', string='Bidang / Departemen Terkait', store=True)
    tanggal_pelaksanaan = fields.Date(string='Tanggal Pelaksanaan', store=True)
    durasi = fields.Char(string='Durasi Pelatihan', store=True)
    tempat = fields.Char(string='Tempat Pelaksanaan', store=True)
    metode = fields.Selection([
        ('tatap_muka', 'Tatap Muka'),
        ('daring', 'Daring'),
        ('blended', 'Blended'),
    ], string='Metode Pelatihan', store=True)
