from odoo import api, fields, models, tools
class Hang_hoa(models.Model):
    _name = "hang.hoa"

    product_name = fields.Char('Tên hàng',required=True)
    manuafacturer = fields.Char('Hãng sản xuất')
    origin_country = fields.Char('Nước sản suất')
    on_hand = fields.Integer("Số lượng tồn kho")
    position = fields.Char("Vị trí hàng hóa")
    cost_price = fields.Float("Số vốn")
    sold_price = fields.Float("Giá bán")
    weight = fields.Float("Trọng lượng")
    packing_spec = fields.Char("Quy cách đóng gói",size=50)
    sell_in_store = fields.Boolean("Bán trực tiếp")
    group = fields.Many2one('nhom.hang.hoa', string='Cấp cha')
    product_no = fields.Char(string='Mã hàng hóa',required=True,copy=False,readonly=True,index=True,default='New')

    @api.model
    def create(self, vals):
        if vals.get('product_no', '/') == '/':
            vals['product_no'] = self.env['ir.sequence'].next_by_code('code.hanghoa') or '/'
        return super(Hang_hoa, self).create(vals)
