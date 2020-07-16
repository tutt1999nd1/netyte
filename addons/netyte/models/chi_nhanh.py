from odoo import api, fields, models, tools
class Chi_nhanh(models.Model):
    _name = "chi.nhanh"

    name = fields.Char('Tên chi nhánh',required=True)
    code = fields.Char('Mã chi nhánh',required=True)
    address = fields.Text("Địa chỉ")
    phone_number = fields.Integer("Số điện thoại",required=True)
    fax_number = fields.Integer("Số fax chi nhánh")
    contact = fields.Char("Người liên hệ")
    province = fields.Many2one('tinh', string="Tỉnh")
    note = fields.Text("Ghi chú")
    default = fields.Boolean("Mặc định")
    time_of_operation = fields.Date("Thời điểm hoạt động")
    logo = fields.Binary("Logo", attachment=True, help="Logo")
    parent_id = fields.Many2one('chi.nhanh',string="Chi nhánh cha")

class Tinh(models.Model):
    _name = "tinh"
    code = fields.Char("Mã tỉnh")
    name = fields.Char("Tên tỉnh")