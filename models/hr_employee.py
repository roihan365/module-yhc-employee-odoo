from odoo import models, fields, api
from datetime import date

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    nrp = fields.Char(string="NRP", store=True)
    area_kerja = fields.Char(string="Area Kerja", store=True)
    # tgl_mulai_kerja = fields.Date(string="Tanggal Mulai Kerja")
    blood_type = fields.Selection([
        ('a','A'), ('b','B'), ('o','O'), ('ab','AB')
    ], string="Golongan Darah", store=True)

    nama_ktp = fields.Char(string="Nama Sesuai KTP", store=True)
    nik = fields.Char(string="NIK", store=True)
    alamat_ktp = fields.Text(string="Alamat Sesuai KTP", store=True)

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
    nama_anak_kandung = fields.Char(string="Nama Anak Kandung", store=True)
    nama_suami_istri = fields.Char(string="Nama Suami/Istri", store=True)
    
     # --- Data Umum ---
    religion = fields.Selection([
        ('islam','Islam'), ('kristen','Kristen'), ('katolik','Katolik'),
        ('hindu','Hindu'), ('buddha','Buddha'), ('konghucu','Konghucu')
    ], string="Agama", store=True)
    structural_position = fields.Char(string="Jabatan Struktural", store=True)
    employment_type = fields.Char(string="Jenis Kepegawaian", store=True)
    section = fields.Char(string="Section", store=True)
    golongan = fields.Char(string="Golongan", store=True)
    grade = fields.Char(string="Grade/Pangkat", store=True)
    nationality = fields.Char(string="Kewarganegaraan", store=True)

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
    employee_category = fields.Selection([
        ('phl', 'PHL'),
        ('spk', 'SPK'),
        ('pkwt', 'PKWT'),
        ('tetap', 'Tetap'),
        ('magang', 'Magang'),
    ], string="Jenis Pegawai", store=True)
    
    # --- Asuransi & Data Lain ---
    insurance_number = fields.Char(string="No. Peserta Asuransi", store=True)
    group_component_code = fields.Char(string="Kode Group Komponen", store=True)
    access_level = fields.Char(string="Level Akses", store=True)
    service_length = fields.Integer(string="Masa Kerja", compute="_compute_service_length", store=True)
    shirt_size = fields.Selection([
        ('s','S'), ('m','M'), ('l','L'), ('xl','XL'), 
        ('xxl','XXL'), ('xxxl','XXXL')
    ], string="Ukuran Baju", store=True)
    appointment = fields.Char(string="Pengangkatan", store=True)
    
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