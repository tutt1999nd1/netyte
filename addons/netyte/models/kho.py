from odoo import api, fields, models, tools
class Kho(models.Model):
    _name = "kho"

    name = fields.Char('Tên kho',required=True)
    store_code = fields.Char('Mã kho',required=True)
    agency = fields.Many2one('chi.nhanh',string="Chi nhánh")
    address = fields.Text("Địa chỉ kho")
    phone_number = fields.Integer("Điện thoại",required=True)
    person_in_charge = fields.Char("NGười phụ trách")
    note = fields.Text("Ghi chú")
    default = fields.Boolean("Mặc định")
    active = fields.Boolean(string="Kích hoạt",default=True)