# -*- coding: utf-8 -*-

from random import randint

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PublicComment(models.Model):
    _name = 'public.comment'
    _description = 'Public user blog comment'

    name = fields.Char('Name', required=True)
    state = fields.Selection([('new','New'), ('validated','Validated')], 'State', default='new', required=True, copy=False, readonly=True)
    email = fields.Char()
    content = fields.Text('Content', required=True)
    limited_content = fields.Text('Content', compute='_compute_limited_content')
    blog_post_id = fields.Many2one('blog.post', 'Blog post', ondelete='cascade', required=True)
    outtxt = fields.Char() # captcha input text
    nb_alea = fields.Integer() # captcha number


    def create(self, vals):
        if vals.get('outtxt') and vals.get('nb_alea'):
            captcha = {
                0: '14391',
                1: '88492',
                2: '39560',
                3: '49865',
                4: '44120',
                5: '80544',
                6: '81338',
                7: '38859',
                8: '78584',
                9: '58133',
            }
            if vals['outtxt'] != captcha[vals['nb_alea']]:
                raise ValidationError('Wrong captcha')
        else:
            raise ValidationError("Comment can't be created because captcha was not provided")
        # we don't need to store these values in the database
        vals.pop('outtxt')
        vals.pop('nb_alea')
        return super(PublicComment, self).create(vals)


    def button_validate_comment(self):
        for record in self:
            record.state = 'validated'   

    def button_back_to_new(self):
        for record in self:
            record.state = 'new'

    def button_unlink(self):
        for record in self:
            record.unlink()
        return self.env.ref('website_blog_public_user_comment.action_blog_public_comments').read()[0]   

    @api.depends('content')
    def _compute_limited_content(self):
        for record in self:
            record.limited_content = record.content[:60].replace('\n', ' ')


class BlogPost(models.Model):
    _inherit = 'blog.post'

    public_comment_ids = fields.One2many('public.comment', 'blog_post_id', 'Public comments')
    validated_comment_ids = fields.One2many('public.comment', compute='_compute_validated_comment_ids')

    @api.depends('public_comment_ids')
    def _compute_validated_comment_ids(self):
        for blog_post in self:
            blog_post.validated_comment_ids = self.env['public.comment'].search([
                ('state', '=', 'validated'),
                ('blog_post_id', '=', blog_post.id),
            ], order='create_date')

    def get_out_img_nb(self):
        return randint(0,9)