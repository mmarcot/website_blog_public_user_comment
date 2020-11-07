# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class website_blog_public_user_comment(models.Model):
#     _name = 'website_blog_public_user_comment.website_blog_public_user_comment'
#     _description = 'website_blog_public_user_comment.website_blog_public_user_comment'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
