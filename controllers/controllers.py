# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteBlogPublicUserComment(http.Controller):
#     @http.route('/website_blog_public_user_comment/website_blog_public_user_comment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_blog_public_user_comment/website_blog_public_user_comment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_blog_public_user_comment.listing', {
#             'root': '/website_blog_public_user_comment/website_blog_public_user_comment',
#             'objects': http.request.env['website_blog_public_user_comment.website_blog_public_user_comment'].search([]),
#         })

#     @http.route('/website_blog_public_user_comment/website_blog_public_user_comment/objects/<model("website_blog_public_user_comment.website_blog_public_user_comment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_blog_public_user_comment.object', {
#             'object': obj
#         })
