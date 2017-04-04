# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'Maple Data',
    'version': '1.0',
    'author': "Portall Solutions inc.",
    'website': "portall.ca",
    'category': 'Maple',
    'summary':  'Maple Data injection in Python',
    'depends': ['maple'],
    'description': """
    Maple Data injection in Python
    """,
    'data': [
     ],
    'qweb': [
    ],     
    'installable': True,
    'application': False,
    'post_init_hook': '_setup_maple',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
