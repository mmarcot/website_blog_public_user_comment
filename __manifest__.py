# -*- coding: utf-8 -*-
{
    'name': "website_blog_public_user_comment",

    'summary': """
        Allow public users to comment on your blog
    """,

    'description': """
        Allow public users to comment on your blog
    """,

    'author': "Mallory MARCOT",
    'website': "https://www.mallory-marcot.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_blog', 'website_form'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/assets.xml',
        'views/templates.xml',
        'data/comment_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
