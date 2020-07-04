from odoo import api, fields, models, tools, _
class Nhom_hang_hoa(models.Model):
    _name = "nhom.hang.hoa"

    name = fields.Char('Nhóm hàng hóa',required=True)
    code = fields.Char('Mã nhóm',required=True)
    status = fields.Selection([
        ('dangkinhdoanh', 'Đang kinh doanh'),
        ('ngungkinhdoanh', 'Ngừng kinh doanh')
    ], string='Trạng thái', default='dangkinhdoanh')
    description = fields.Char('Mô tả')
    parent_id = fields.Many2one('nhom.hang.hoa', string='Cấp cha')
