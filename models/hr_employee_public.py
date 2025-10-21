from odoo import models, fields

class HrEmployeePublic(models.Model):
    _inherit = "hr.employee.public"

    # --- Data Custom (related dari hr.employee) ---
    nrp = fields.Char(related="employee_id.nrp", readonly=True)
    area_kerja_id = fields.Many2one('employee_id.area_kerja_id', readonly=True)
    blood_type = fields.Selection(
        related="employee_id.blood_type",
        readonly=True
    )
    nama_ktp = fields.Char(related="employee_id.nama_ktp", readonly=True)
    nik = fields.Char(related="employee_id.nik", readonly=True)
    alamat_ktp = fields.Text(related="employee_id.alamat_ktp", readonly=True)

    alamat_kk = fields.Text(related="employee_id.alamat_kk", readonly=True)
    birthday_kk = fields.Date(related="employee_id.birthday_kk", readonly=True)
    nik_kk = fields.Char(related="employee_id.nik_kk", readonly=True)
    no_kk = fields.Char(related="employee_id.no_kk", readonly=True)

    no_akta = fields.Char(related="employee_id.no_akta", readonly=True)
    nama_akta = fields.Date(related="employee_id.nama_akta", readonly=True)
    birthday_akta = fields.Date(related="employee_id.birthday_akta", readonly=True)

    place_of_birth = fields.Char(related="employee_id.place_of_birth", readonly=True)
    age = fields.Integer(related="employee_id.age", readonly=True)
    birthday = fields.Date(related="employee_id.birthday", readonly=True)
    gender = fields.Selection(related="employee_id.gender", readonly=True)

    npwp = fields.Char(related="employee_id.npwp", readonly=True)
    status_kawin = fields.Selection(related="employee_id.status_kawin", readonly=True)
    status_pajak = fields.Selection(related="employee_id.status_pajak", readonly=True)
    tanggungan_pajak = fields.Integer(related="employee_id.tanggungan_pajak", readonly=True)
    jlh_anggota_keluarga = fields.Integer(related="employee_id.jlh_anggota_keluarga", readonly=True)
    nama_ibu_kandung = fields.Char(related="employee_id.nama_ibu_kandung", readonly=True)
    nama_ayah_kandung = fields.Char(related="employee_id.nama_ayah_kandung", readonly=True)
    nama_mertua = fields.Char(related="employee_id.nama_mertua", readonly=True)
    nama_anak_kandung = fields.Char(related="employee_id.nama_anak_kandung", readonly=True)
    nama_suami_istri = fields.Char(related="employee_id.nama_suami_istri", readonly=True)

    # --- Data Umum ---
    religion = fields.Selection(related="employee_id.religion", readonly=True)
    structural_position = fields.Char(related="employee_id.structural_position", readonly=True)
    employment_type = fields.Char(related="employee_id.employment_type", readonly=True)
    section = fields.Char(related="employee_id.section", readonly=True)
    golongan_id = fields.Many2one('employee_id.area_kerja_id.golongan', readonly=True)
    grade_id = fields.Many2one('employee_id.area_kerja_id.grade', readonly=True)
    nationality = fields.Char(related="employee_id.nationality", readonly=True)

    # --- Status Pekerjaan ---
    first_contract_date = fields.Date(related="employee_id.first_contract_date", readonly=True)
    termination_date = fields.Date(related="employee_id.termination_date", readonly=True)
    employment_status = fields.Selection(related="employee_id.employment_status", readonly=True)
    income_start = fields.Date(related="employee_id.income_start", readonly=True)
    income_end = fields.Date(related="employee_id.income_end", readonly=True)
    employment_method = fields.Char(related="employee_id.employment_method", readonly=True)
    # employee_category = fields.Selection(related="employee_id.employee_category", readonly=True)
    employee_category_id = fields.Many2one('employee_id.area_kerja_id.category', readonly=True)
    employee_type_id = fields.Many2one('employee_id.area_kerja_id.type', readonly=True)

    # --- Asuransi & Data Lain ---
    insurance_number = fields.Char(related="employee_id.insurance_number", readonly=True)
    group_component_code = fields.Char(related="employee_id.group_component_code", readonly=True)
    access_level = fields.Char(related="employee_id.access_level", readonly=True)
    service_length = fields.Integer(related="employee_id.service_length", readonly=True)
    shirt_size = fields.Selection(related="employee_id.shirt_size", readonly=True)
    body_weight = fields.Float(string="Berat Badan (kg)", readonly=True)
    body_height = fields.Float(string="Tinggi Badan (cm)", readonly=True)
    pants_size = fields.Char(string="Ukuran Celana", readonly=True)
    appointment = fields.Char(string="Pengangkatan", readonly=True)
    appointment = fields.Char(related="employee_id.appointment", readonly=True)

    # --- Relasi One2many ---
    bpjs_ids = fields.One2many(related="employee_id.bpjs_ids", readonly=True)
    education_ids = fields.One2many(related="employee_id.education_ids", readonly=True)
    payroll_ids = fields.One2many(related="employee_id.payroll_ids", readonly=True)
    
    
