from odoo import models, fields

class HrEmployeePayroll(models.Model):
    _name = "hr.employee.payroll"
    _description = "Data Payroll Karyawan"

    employee_id = fields.Many2one("hr.employee", string="Karyawan", ondelete="cascade", required=True)

    bank_name = fields.Char(string="Nama Bank")
    bank_account = fields.Char(string="No. Rekening")
    bank_branch = fields.Char(string="Cabang Bank")
    account_holder = fields.Char(string="Atas Nama Rekening")
    tanggal_payroll = fields.Date(string="Tanggal Masuk Payroll")