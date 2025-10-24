from odoo import models, fields

class HrTrainingCertificate(models.Model):
    _name = 'hr.training.certificate'
    _description = 'Sertifikat Pelatihan Karyawan'

    employee_id = fields.Many2one('hr.employee', string='Karyawan', ondelete='cascade')
    name = fields.Char(string='Nama Pelatihan', required=True)
    tujuan = fields.Text(string='Tujuan Pelatihan')
    jenis_pelatihan = fields.Selection([
        ('internal', 'Internal'),
        ('eksternal', 'Eksternal'),
        ('teknis', 'Teknis'),
        ('nonteknis', 'Nonteknis'),
    ], string='Jenis Pelatihan')
    department_id = fields.Many2one('hr.department', string='Bidang / Departemen Terkait')
    tanggal_pelaksanaan = fields.Date(string='Tanggal Pelaksanaan')
    durasi = fields.Char(string='Durasi Pelatihan')
    tempat = fields.Char(string='Tempat Pelaksanaan')
    metode = fields.Selection([
        ('tatap_muka', 'Tatap Muka'),
        ('daring', 'Daring'),
        ('blended', 'Blended'),
    ], string='Metode Pelatihan')
