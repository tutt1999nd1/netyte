from odoo import api, fields, models, tools
class Hang_hoa(models.Model):
    _name = "hang.hoa"
    name = fields.Char('Tên hàng',required = True)
    on_hand = fields.Integer("Tồn kho")
    position = fields.Char("Vị trí")
    cost_price = fields.Float("Gía vốn")
    sold_price = fields.Float("Giá bán")
    sold_price_combo = fields.Float("Giá bán combo",compute='_sum_price')
    weight = fields.Float("Trọng lượng")
    packing_spec = fields.Char("Quy cách đóng gói",size = 50)
    sell_in_store = fields.Boolean("Bán trực tiếp")
    group = fields.Many2one('nhom.hang.hoa', string='Cấp cha')
    product_no = fields.Char(string='Mã hàng hóa',required=True,copy=False,readonly=True,index=True,default='New')
    group = fields.Many2one('nhom.hang.hoa', string = 'Nhóm hàng hóa')
    product_no = fields.Char(string = 'Mã hàng hóa',required = True,copy = False,index = True)
    origin_country = fields.Many2one("dat.nuoc",string = "Nước sản xuất")
    manuafacturer = fields.Many2one("nha.san.xuat",string = "Hãng sản xuất")
    don_vi = fields.Many2one("don.vi", string = "Đơn vị")
    description = fields.Text("Mô tả")
    roa = fields.Char("Đường dùng" ,size=100)
    reg_number = fields.Char("Số đăng ký",size=12)
    active_ingredients = fields.Char("Hoạt chất",size = 200)
    ham_luong = fields.Char("Hàm lượng",size = 200)

    type = fields.Selection([
        ('hanghoa', 'Hàng hóa'),
        ('thuoc', 'Thuốc'),
        ('combo','Combo - Đóng gói')
    ], string='Thể loại', default='hanghoa')
    components = fields.Many2many(
        comodel_name="hang.hoa",
        relation="hang_hoa_hang_hoa_rel",
        column1="hang_hoa_parent_id",
        column2="hang_hoa_id",
        string="Thành phần"
    )

    @api.model
    def create(self, vals):
        if vals.get('product_no', '/') == '/':
            vals['product_no'] = self.env['ir.sequence'].next_by_code('code.hanghoa') or '/'
        return super(Hang_hoa, self).create(vals)

    @api.depends('sold_price_combo')
    def _sum_price(self):
        for record in self:
            for record2 in record.components:
                record.sold_price_combo= record.sold_price_combo + record2.sold_price

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




