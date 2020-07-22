from odoo import api, fields, models, tools
class Khach_hanh(models.Model):
    _name = "nhan.vien"

    name = fields.Char('Tên nhân viên',required=True)
    employee_id = fields.Char('Mã nhân viên',required=True)
    phone_number = fields.Integer("Số điện thoại",required=True)
    date_of_birth = fields.Date("Ngày sinh")
    identity_card_number = fields.Char('Số chứng minh thư nhân dân', required=True)
    department = fields.Many2one('phong.ban',string="Phòng ban")
    professional_titles = fields.Many2one('chuc.danh',string="Chức danh")
    agency = fields.Many2one('chi.nhanh',string="Chi nhánh làm việc")
    facebook = fields.Char("Facebook")
    sex = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ')
    ], string='Giới tính', default='male')
    address = fields.Text("Địa chỉ")
    wards = fields.Many2one('huyen', string="Phường/Huyện")
    province = fields.Many2one('tinh', string="Tỉnh")
    email = fields.Char("Email")
    note = fields.Text("Ghi chú")
    avatar = fields.Binary("Ảnh", attachment=True, help="avatar")

class Phong_ban(models.Model):
    _name = "phong.ban"

    name = fields.Char("Tên phòng ban")
    description = fields.Char("Mô tả")
    status = fields.Selection([
        ('active', 'Đang hoạt động'),
        ('deactive', 'Ngừng hoạt động')
    ], string='Trạng thái', default='active')

class Chuc_danh(models.Model):
    _name = "chuc.danh"

    name = fields.Char("Tên chức danh")
    description = fields.Char("Mô tả")
    status = fields.Selection([
        ('active', 'Đang hoạt động'),
        ('deactive', 'Ngừng hoạt động')
    ], string='Trạng thái', default='active')