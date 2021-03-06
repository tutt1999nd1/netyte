# -*- coding: utf-8 -*-
{
    'name': "Netyte",
    'summary': """Netyte""",
    'description': """Managing pet information""",
    'author': "tu truong",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'views/nhom_hang_hoa.xml',
        'views/hang_hoa.xml',
        'views/listview_templates.xml',
        'views/menu.xml',
        'views/don_thuoc.xml',
        'views/chi_nhanh.xml',
        'views/nha_cung_cap.xml',
        'views/khach_hang.xml',
        'views/kho.xml',
        'views/bac_si.xml',
        'views/nhan_vien.xml',

    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
