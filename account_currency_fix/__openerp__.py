# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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


{
    'name': 'Second Currency Auto Switching to Debit/Credit',
    'version': '1.0',
    'category' : 'Accounting & Finance',
    'description': """
OSCG Currency Fix-Accounting
==========================

OSCG specially designed this module to solve Multi-Currency problem for Odoo.
If you need some helps, contact us(http://www.oscg.com.hk/).

User Instructions
------------
The module will calculate the Debit or Credit amount per your Company Currency from the Second Currency you input in the Journal Entry automatically.
When you successfully install this module, it adds a menu under Accounting->Journal Entries->Manual Entries.
Please note you need to:
1. Choose Currency first.
2. Input Amount Currency amount, input positive amount if you want it to be shown in Debit side and input negative amount if you want it to be shown in Credit Side.
3. Hit Tab, the Debit/Credit in the journal entry will be automatically updated.
4. You are free to change Debit/Credit value while it will not affect the amount currency.

    """,
    'author': 'OSCG',
    'depends': ['account'],
    'images': [],
    'data': ['account_view.xml'],
    'demo': [],
    'test': [],
    'website': 'http://www.oscg.com.hk',
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
