from odoo import api, fields, models, tools
class Hang_hoa(models.Model):
    _name = "hang.hoa"
    name = fields.Char('Tên hàng',required = True)
    on_hand = fields.Integer("Tồn kho")
    position = fields.Char("Vị trí")
    cost_price = fields.Float("Gía vốn")
    sold_price = fields.Float("Giá bán",compute='_tien')
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
    don_vi_tinh = fields.Many2one("don.vi", string = "Đơn vị")
    don_vi = fields.One2many(
        'don.vi.to','don_vi_to_id',string= "Danh sách đơn vị",select = True
    )
    description = fields.Text("Mô tả")
    roa = fields.Char("Đường dùng" ,size=100)
    reg_number = fields.Char("Số đăng ký",size=12)
    active_ingredients = fields.Char("Hoạt chất",size = 200)
    ham_luong = fields.Char("Hàm lượng",size = 200)
    thuoc = fields.Many2one('thuoc', string ='Tên thuốc')

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
    # tính tiền theo đơn vị
    @api.onchange('don_vi_tinh')
    def _tien(self):
        print("check")
        for record in self:
            record.sold_price = 0
            for don_vi in record.don_vi:
                if don_vi.name == record.don_vi_tinh.name:
                    record.sold_price = don_vi.gia_ban

    @api.onchange('components')
    def _sum_price(self):
        for record in self:
            record.sold_price_combo=0
            if not record.components:
                record.sold_price_combo = 0
            if record.components:
                for record2 in record.components:
                    record.sold_price_combo= record.sold_price_combo + record2.sold_price
                record.sold_price = record.sold_price_combo

    @api.onchange('thuoc')
    def _change_info_thuoc(self):
        self.reg_number=self.thuoc.reg_number
        self.active_ingredients=self.thuoc.active_ingredients
        self.ham_luong=self.thuoc.ham_luong
        self.packing_spec=self.thuoc.packing_spec
        self.manuafacturer=self.thuoc.manuafacturer
        self.origin_country=self.thuoc.origin_country

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
    name = fields.Char("Tên đơn vị")
class Don_vi_to(models.Model):
    _name = "don.vi.to"
    name = fields.Char("Đơn vị")
    gia_ban= fields.Float("Giá bán")
    don_vi=fields.Many2one("don.vi",string='Đơn vị')
    don_vi_to_id=fields.Many2one('hang.hoa',string="Hàng hóa")

class Thuoc(models.Model):
    _name = "thuoc"
    name = fields.Char("Tên thuốc")
    reg_number = fields.Char("Số đăng ký", size=12)
    active_ingredients = fields.Char("Hoạt chất", size=200)
    ham_luong = fields.Char("Hàm lượng", size=200)
    origin_country = fields.Many2one("dat.nuoc", string="Nước sản xuất")
    manuafacturer = fields.Many2one("nha.san.xuat", string="Hãng sản xuất")
    packing_spec = fields.Char("Quy cách đóng gói",size = 50)

