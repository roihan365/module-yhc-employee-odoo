from odoo import models, fields

class HrEmployeeRewardPunishment(models.Model):
    _name = 'hr.employee.reward.punishment'
    _description = 'Reward & Punishment Karyawan'
    _order = 'date desc'

    employee_id = fields.Many2one('hr.employee', string='Karyawan', required=True, ondelete='cascade')

    type = fields.Selection([
        ('reward', 'Reward'),
        ('punishment', 'Punishment'),
    ], string='Tipe', required=True, default='reward', store=True)

    reward_category = fields.Selection([
        ('gathering', 'Gathering'),
        ('program_sekolah', 'Program Sekolah'),
        ('program_yayasan', 'Program Yayasan'),
    ], string='Kategori Reward', store=True)

    punishment_category = fields.Selection([
        ('st1', 'Surat Teguran 1'),
        ('st2', 'Surat Teguran 2'),
        ('st3', 'Surat Teguran 3'),
        ('sp1', 'Surat Peringatan 1'),
        ('sp2', 'Surat Peringatan 2'),
        ('sp3', 'Surat Peringatan 3'),
    ], string='Kategori Punishment', store=True)

    date = fields.Date(string='Tanggal', default=fields.Date.context_today, store=True)

    supporting = fields.Binary("Bukti Pendukung")
    supporting_filename = fields.Char("Bukti Filename")
    description = fields.Char(string='Keterangan')
