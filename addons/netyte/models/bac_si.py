from odoo import api, fields, models, tools
class Bac_si(models.Model):
    _name = "bac.si"

    name = fields.Char('Tên bác sĩ',required=True)
    doctor_id = fields.Char('Mã bác sĩ',required=True)
    sex = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ')
    ], string='Giới tính', default='male')
    specialist = fields.Many2one('chuyen.khoa',string="Chuyên khoa")
    qualification = fields.Many2one('trinh.do',string="Trình độ")
    work_place = fields.Many2one('work.place',string="Nơi công tác")
    status = fields.Selection([
        ('active', 'Đang hoạt động'),
        ('deavtice', 'Ngừng hoạt động')
    ], string='Trạng thái', default='active')
    phone_number = fields.Integer("Số điện thoại",required=True)
    address = fields.Text("Địa chỉ")
    wards = fields.Many2one('huyen',string="Phường/Huyện")
    province = fields.Many2one('tinh', string="Tỉnh")
    email = fields.Char("Email")
    note = fields.Text("Ghi chú")
    image = fields.Binary("Ảnh", attachment=True, help="Logo")

class Chuyen_khoa(models.Model):
    _name = "chuyen.khoa"

    name = fields.Char("Tên chuyên khoa")

class Trinh_do(models.Model):
    _name = "trinh.do"

    name = fields.Char("Trình độ")

class Work_place(models.Model):
    _name = "work.place"

    name = fields.Char("Tên nơi công tác")