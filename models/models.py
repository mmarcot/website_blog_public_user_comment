# -*- coding: utf-8 -*-

from odoo import models, fields, api


class website_blog_public_user_comment(models.Model):
    _name = 'website_blog_public_user_comment.comment'
    _description = 'Public user blog comment'

    name = fields.Char()
    email = fields.Char()
    content = fields.Text()

