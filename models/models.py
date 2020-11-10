# -*- coding: utf-8 -*-

from odoo import models, fields, api


class website_blog_public_user_comment(models.Model):
    _name = 'website_blog_public_user_comment.comment'
    _description = 'Public user blog comment'

    name = fields.Char()
    email = fields.Char()
    content = fields.Text()
    blog_post_id = fields.Many2one('blog.post', 'Blog post', ondelete='cascade', required=True)


class BlogPost(models.Model):
    _inherit = 'blog.post'

    public_comment_ids = fields.One2many('website_blog_public_user_comment.comment', 'blog_post_id', 'Public comments')