from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    nrp = fields.Char(string="NRP", store=True)
    gelar = fields.Char(string="Gelar", help="Gelar akademik atau profesional")
    area_kerja_id = fields.Many2one('hr.employee.area_kerja', string="Area Kerja")
    # tgl_mulai_kerja = fields.Date(string="Tanggal Mulai Kerja")
    blood_type = fields.Selection([
        ('a','A'), ('b','B'), ('o','O'), ('ab','AB')
    ], string="Golongan Darah", store=True)

    nama_ktp = fields.Char(string="Nama Sesuai KTP", store=True)
    nik = fields.Char(string="NIK", store=True)
    alamat_ktp = fields.Text(string="Alamat Sesuai KTP", store=True)
    alamat_domisili = fields.Text(string="Alamat Domisili", store=True)
    alamat_kk = fields.Text(string="Alamat Sesuai KK", store=True)
    birthday_kk = fields.Date(string="Tanggal Lahir Sesuai KK", store=True)
    nik_kk = fields.Char(string="NIK Sesuai KK", store=True)
    no_kk = fields.Char(string="No. KK", store=True)    
    
    no_akta = fields.Char(string="No. Akta Lahir", store=True)
    nama_akta = fields.Date(string="Nama Sesuai Akta", store=True)
    birthday_akta = fields.Date(string="Tanggal Lahir Sesuai Akta", store=True)

    age = fields.Integer(string="Usia", compute="_compute_age", store=True)
    
    bpjs_ids = fields.One2many("hr.employee.bpjs", "employee_id", string="BPJS")
    education_ids = fields.One2many("hr.employee.education", "employee_id", string="Riwayat Pendidikan")
    payroll_ids = fields.One2many("hr.employee.payroll", "employee_id", string="Payroll")

    @api.depends('birthday')
    def _compute_age(self):
        """Hitung usia otomatis berdasarkan tanggal lahir."""
        today = date.today()
        for rec in self:
            if rec.birthday:
                rec.age = (
                    today.year - rec.birthday.year
                    - ((today.month, today.day) < (rec.birthday.month, rec.birthday.day))
                )
            else:
                rec.age = 0
                
    npwp = fields.Char(string="NPWP")
    npwp_registration_date = fields.Char(string="Tanggal Terdaftar")
    npwp_address = fields.Char(string="Alamat NPWP")
    efin = fields.Char(string="EFIN")
    status_kawin = fields.Selection([
        ('kawin','Kawin'), ('lajang','Lajang'), ('cerai','Cerai')
    ], string="Status Perkawinan", store=True)
    status_pajak = fields.Selection([
        ('tk0','TK/0'), ('tk1','TK/1'), ('tk2','TK/2'), ('tk3','TK/3'),
        ('k0','K/0'), ('k1','K/1'), ('k2','K/2'), ('k3','K/3'), ('k10', 'K1/0'),
        ('k11','K1/1'), ('k12','K1/2'), ('k13','K1/3')
    ], string="Status Pajak", store=True)
    tanggungan_pajak = fields.Integer(string="Tanggungan (Pajak)", store=True)
    jlh_anggota_keluarga = fields.Integer(string="Jumlah Anggota Keluarga", store=True)
    nama_ibu_kandung = fields.Char(string="Nama Ibu Kandung", store=True)
    nama_ayah_kandung = fields.Char(string="Nama Ayah Kandung", store=True)
    nama_mertua = fields.Char(string="Nama Mertua", store=True)
    family_child_ids = fields.One2many(
        'yhc.employee.child',
        'employee_id',
        string='Data Anak Kandung'
    )
    nama_suami_istri = fields.Char(string="Nama Suami/Istri", store=True)
    
     # --- Data Umum ---
    religion = fields.Selection([
        ('islam','Islam'), ('kristen','Kristen'), ('katolik','Katolik'),
        ('hindu','Hindu'), ('buddha','Buddha'), ('konghucu','Konghucu')
    ], string="Agama", store=True)
    structural_position = fields.Char(string="Jabatan Struktural", store=True)
    employment_type = fields.Char(string="Jenis Kepegawaian", store=True)
    section = fields.Char(string="Section", store=True)
    golongan_id = fields.Many2one('hr.employee.golongan', string="Golongan")
    grade_id = fields.Many2one('hr.employee.grade', string="Grade/Pangkat")
    nationality = fields.Char(string="Kewarganegaraan", store=True)
    passport_number = fields.Char(string="Nomor Passport", store=True)
    passport_expiry_date = fields.Date(string="Tanggal Habis Berlaku Passpost", store=True)

    # --- Status Pekerjaan ---
    first_contract_date = fields.Date(string="Tanggal Kontrak Pertama", store=True)
    tanggal_pengangkatan = fields.Date(string="Tanggal Pengangkatan", store=True)
    termination_date = fields.Date(string="Tanggal Berhenti", store=True)
    employment_status = fields.Selection([
        ('aktif', 'Aktif'),
        ('nonaktif', 'Non Aktif'),
        ('pensiun', 'Pensiun')
    ], string="Status Kepegawaian", store=True)
    income_start = fields.Date(string="Masa Penghasilan Awal", store=True)
    income_end = fields.Date(string="Masa Penghasilan Akhir", store=True)
    employment_method = fields.Char(string="Metode", store=True)
    # employee_type = fields.Selection(
    #     related="user_id.employee_type",
    #     string="Jenis Pegawai",
    #     readonly=False,   
    #     store=True
    # )
    employee_category_id = fields.Many2one('hr.employee.category', string="Jenis Pegawai")
    employee_type_id = fields.Many2one('hr.employee.type', string="Tipe Pegawai")
    kota_asal = fields.Char(
            related='private_city',
            string='Kota Asal',
            store=True,
            readonly=False
        )
    provinsi_asal = fields.Many2one(
        related='private_state_id',
        string='Provinsi Asal',
        store=True,
        readonly=False,
        domain=[]
    )
    
    # --- Asuransi & Data Lain ---
    insurance_number = fields.Char(string="No. Peserta Asuransi", store=True)
    group_component_code = fields.Char(string="Kode Group Komponen", store=True)
    access_level = fields.Char(string="Level Akses", store=True)
    service_length = fields.Integer(string="Masa Kerja", compute="_compute_service_length", store=True)
    shirt_size = fields.Selection([
        ('s','S'), ('m','M'), ('l','L'), ('xl','XL'), 
        ('xxl','XXL'), ('xxxl','XXXL')
    ], string="Ukuran Baju", store=True)
    body_weight = fields.Float(string="Berat Badan (kg)", store=True)
    body_height = fields.Float(string="Tinggi Badan (cm)", store=True)
    pants_size = fields.Char(string="Ukuran Celana", store=True)
    appointment = fields.Char(string="Pengangkatan", store=True)
    
    reward_punishment_ids = fields.One2many(
        'hr.employee.reward.punishment',
        'employee_id',
        string='Reward & Punishment'
    )
    
    # --- Compute Masa Kerja ---
    @api.depends('birthday', 'termination_date')
    def _compute_service_length(self):
        """
        Hitung masa kerja (tahun) berdasarkan tanggal mulai kerja 
        dan tanggal berhenti (jika ada).
        """
        today = date.today()
        for rec in self:
            start = rec.first_contract_date or rec.create_date.date() if rec.create_date else None
            end = rec.termination_date or today
            if start:
                rec.service_length = end.year - start.year - (
                    (end.month, end.day) < (start.month, start.day)
                )
            else:
                rec.service_length = 0
                
    @api.constrains('passport_number')
    def _check_passport_number(self):
        for rec in self:
            if rec.passport_number and not rec.passport_number.isdigit():
                raise ValidationError("Nomor Passport hanya boleh berisi angka saja!")
                

class EmployeeGolongan(models.Model):
    _name = 'hr.employee.golongan'
    _description = 'Golongan Pegawai'

    name = fields.Char(string='Golongan', required=True)

class EmployeeGrade(models.Model):
    _name = 'hr.employee.grade'
    _description = 'Grade atau Pangkat Pegawai'

    name = fields.Char(string='Grade/Pangkat', required=True)

class EmployeeCategory(models.Model):
    _name = 'hr.employee.category'
    _description = 'Jenis Pegawai'

    name = fields.Char(string='Jenis Pegawai', required=True)
    color = fields.Integer(string='Color Index', default=0)

class EmployeeType(models.Model):
    _name = 'hr.employee.type'
    _description = 'Tipe Pegawai'

    name = fields.Char(string='Tipe Pegawai', required=True)
    
class EmployeeAreaKerja(models.Model):
    _name = 'hr.employee.area_kerja'
    _description = 'Area Kerja'

    name = fields.Char(string='Area Kerja', required=True)