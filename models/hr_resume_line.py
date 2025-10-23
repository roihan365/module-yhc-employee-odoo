# file: models/hr_resume_line_inherit.py
from odoo import models, fields

class HrResumeLine(models.Model):
    _inherit = 'hr.resume.line'

    training_method = fields.Selection([
        ('tatap_muka', 'Tatap Muka'),
        ('daring', 'Daring'),
        ('blended', 'Blended'),
    ], string='Metode Pelatihan')

    training_location = fields.Char(string='Tempat Pelatihan')
    training_duration = fields.Float(string='Durasi (hari)')
    supporting_url = fields.Char(string='Bukti Pendukung', help='dokumen/sertifikat pendukung pelatihan')