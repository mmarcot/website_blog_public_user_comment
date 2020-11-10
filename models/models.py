# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PublicComment(models.Model):
    _name = 'public.comment'
    _description = 'Public user blog comment'

    name = fields.Char('Name', required=True)
    state = fields.Selection([('new','New'), ('validated','Validated'), ('rejected','Rejected')], 'State', default='new', required=True)
    email = fields.Char()
    content = fields.Text('Content', required=True)
    blog_post_id = fields.Many2one('blog.post', 'Blog post', ondelete='cascade', required=True)

    def validate_comment(self):
        for record in self:
            record.state = 'validated'          


class BlogPost(models.Model):
    _inherit = 'blog.post'

    public_comment_ids = fields.One2many('public.comment', 'blog_post_id', 'Public comments')