# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Yannick Vaucher
#    Copyright 2012 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{'name': 'Partner Affilates',
 'version': '1.0',
 'author': 'Camptocamp',
 'maintainer': 'Camptocamp',
 'category': 'CRM',
 'complexity': 'normal',  # easy, normal, expert
 'depends': ['base'],
 'description': """Allows to use parent_id in company partner to refer to a parent company
 Plus will show a tab in parent company of affiliated companies""",
 'website': 'http://www.camptocamp.com',
 'init_xml': [],
 'update_xml': [
     'res_partner_view.xml',
     ],
 'demo_xml': [],
 'tests': [],
 'installable': False,
 'images': [],
 'auto_install': False,
 'license': 'AGPL-3',
 'application': True}

