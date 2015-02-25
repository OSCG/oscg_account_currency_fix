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

from openerp.tools.translate import _
from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp

class account_move_line(osv.osv):
    _inherit = "account.move.line"
    _columns = {
        'currency_rate': fields.float('Rate', digits_compute=dp.get_precision('Account')),
    }
    
    def onchange_currency(self, cr, uid, ids, account_id, amount, currency_id, currency_rate=False, date=False, journal=False, context=None):
        if context is None:
            context = {}
        account_obj = self.pool.get('account.account')
        journal_obj = self.pool.get('account.journal')
        currency_obj = self.pool.get('res.currency')
        if (not currency_id) or (not account_id):
            return {}
        result = {}
        acc = account_obj.browse(cr, uid, account_id, context=context)
        if (amount>0) and journal:
            x = journal_obj.browse(cr, uid, journal).default_credit_account_id
            if x: acc = x
        context.update({
                'date': date,
                'res.currency.compute.account': acc,
            })
        v = 0
        if not currency_rate:
            currency_rate = currency_obj.browse(cr, uid, currency_id).rate
            currency_rate = currency_rate and 1/currency_rate
            v = currency_obj.compute(cr, uid, currency_id, acc.company_id.currency_id.id, amount, context=context)
            result['value'] = {
                'debit': v > 0 and v or 0.0,
                'credit': v < 0 and -v or 0.0,
                'currency_rate': currency_rate or 0.0
            }
        else:
            v = amount and amount * currency_rate
            result['value'] = {
                'debit': v > 0 and v or 0.0,
                'credit': v < 0 and -v or 0.0
            }
        return result

account_move_line()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
