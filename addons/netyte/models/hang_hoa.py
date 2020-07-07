from odoo import api, fields, models, tools
class Hang_hoa(models.Model):
    _name = "hang.hoa"
    product_name = fields.Char('Tên hàng',required = True)
    on_hand = fields.Integer("Số lượng tồn kho")
    position = fields.Char("Vị trí hàng hóa")
    cost_price = fields.Float("Số vốn")
    sold_price = fields.Float("Giá bán")
    weight = fields.Float("Trọng lượng")
    packing_spec = fields.Char("Quy cách đóng gói",size = 50)
    sell_in_store = fields.Boolean("Bán trực tiếp")
    group = fields.Many2one('nhom.hang.hoa', string = 'Nhóm hàng hóa')
    product_no = fields.Char(string = 'Mã hàng hóa',required = True,copy = False,readonly = True,index = True,default = 'New')
    origin_country = fields.Many2one("dat.nuoc",string = "Xuất sứ")
    manuafacturer = fields.Many2one("nha.san.xuat",string = "Nhà sản xuất")
    don_vi = fields.Many2one("don.vi", string = "Đơn vị")
    @api.model
    def create(self, vals):
        if vals.get('product_no', '/') == '/':
            vals['product_no'] = self.env['ir.sequence'].next_by_code('code.hanghoa') or '/'
        return super(Hang_hoa, self).create(vals)

class Dat_nuoc(models.Model):
    _name = "dat.nuoc"
    code = fields.Char("Mã")
    name = fields.Char("Tên đất nước")

class Nha_san_xuat(models.Model):
    _name = "nha.san.xuat"
    code = fields.Char("Mã")
    name = fields.Char("Tên nhà sản xuất")

class Don_vi(models.Model):
    _name = "don.vi"
    name = fields.Char("Đơn vị")



