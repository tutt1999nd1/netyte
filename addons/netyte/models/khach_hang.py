from odoo import api, fields, models, tools
class Khach_hanh(models.Model):
    _name = "khach.hang"

    name = fields.Char('Tên khách hàng',required=True)
    customer_id = fields.Char('Mã khách hàng',required=True)
    phone_number = fields.Integer("Số điện thoại",required=True)
    address = fields.Text("Địa chỉ")
    province = fields.Many2one('tinh', string="Tỉnh")
    date_of_birth = fields.Date("Ngày sinh")
    facebook = fields.Char("Facebook")
    tax_code = fields.Char("Mã số thuế")
    sex = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ')
    ], string='Giới tính', default='male')
    email = fields.Char("Email")
    note = fields.Text("Ghi chú")
    status = fields.Boolean(string="Đang hoạt động", default=True)
    logo = fields.Binary("Logo", attachment=True, help="Logo")
    parent_id = fields.Many2one('khach.hang',string="Nhóm khách hàng")
    customer_type = fields.Selection([
        ('personal', 'Cá nhân'),
        ('company', 'Công ty')
    ], string='Loại khách hàng', default='personal')
