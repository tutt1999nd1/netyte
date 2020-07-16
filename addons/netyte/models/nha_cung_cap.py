from odoo import api, fields, models, tools
class Nha_cung_cap(models.Model):
    _name = "nha.cung.cap"

    name = fields.Char('Tên nhà cung cấp',required=True)
    code = fields.Char('Mã nhà cung cấp',required=True)
    address = fields.Text("Địa chỉ")
    phone_number = fields.Integer("Số điện thoại",required=True)
    email = fields.Char("Email")
    wards = fields.Char("Phường/Xã")
    province = fields.Many2one('tinh', string="Tỉnh")
    company = fields.Char("Công ty")
    tax_code = fields.Char("Mã số thuế")
    agency = fields.Many2one("chi.nhanh",string="Chi nhánh")
    note = fields.Text("Ghi chú")
    parent_id = fields.Many2one('nha.cung.cap',string="Nhóm nhà cung cấp")
