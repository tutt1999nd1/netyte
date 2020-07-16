from odoo import api, fields, models, tools
class Don_thuoc(models.Model):
    _name = "don.thuoc"


    name = fields.Char('Tên đơn thuốc',required = True)
    ma_don_thuoc = fields.Char(string = 'Mã đơn thuốc',required = True,copy = False,index = True)
    status = fields.Selection([
        ('apply', 'Áp dung'),
        ('no_apply', 'Chưa áp dụng')
    ], string='Trạng thái', default='apply')
    note = fields.Text("Ghi chú")
    creator = fields.Char("Người tạo")

    @api.model
    def create(self, vals):
        if vals.get('ma_don_thuoc', '/') == '/':
            vals['ma_don_thuoc'] = self.env['ir.sequence'].next_by_code('code.donthuoc') or '/'
        return super(Don_thuoc, self).create(vals)
