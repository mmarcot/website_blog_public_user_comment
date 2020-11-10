# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PublicComment(models.Model):
    _name = 'public.comment'
    _description = 'Public user blog comment'

    name = fields.Char()
    email = fields.Char()
    content = fields.Text()
    blog_post_id = fields.Many2one('blog.post', 'Blog post', ondelete='cascade', required=True)


class BlogPost(models.Model):
    _inherit = 'blog.post'

    public_comment_ids = fields.One2many('public.comment', 'blog_post_id', 'Public comments')