from odoo import models, fields

class HrEmployeeBpjs(models.Model):
    _name = "hr.employee.bpjs"
    _description = "Data BPJS Employee"

    employee_id = fields.Many2one("hr.employee", string="Karyawan", ondelete="cascade")

    bpjs_type = fields.Selection([
        ("ketenagakerjaan", "BPJS Ketenagakerjaan"),
        ("kesehatan", "BPJS Kesehatan"),
    ], string="Jenis BPJS", required=True)

    number = fields.Char(string="Nomor BPJS", required=True)
    nik = fields.Char(string="NIK sesuai KJP")
    registration_number = fields.Date(string="Tanggal Daftar")
    faskes_tk1 = fields.Char(string="Faskes TK I") 
    bpjs_image = fields.Binary("BPJS Image")
    bpjs_image_filename = fields.Char("Image Filename")