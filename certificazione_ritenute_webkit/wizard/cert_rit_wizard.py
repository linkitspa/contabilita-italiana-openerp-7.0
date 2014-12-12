# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright Camptocamp SA 2011
#    Copyright (C) 2013 Associazione OpenERP Italia
#    (<http://www.openerp-italia.org>). 
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

from openerp.osv import fields, orm, osv
from tools.translate import _

class account_print_cert_rit(osv.osv_memory):
    _inherit = "account.common.account.report"
    _name="account.print.cert_rit"
    
    def _get_partner_ids(self, cr, uid, context=None):
        return self.pool.get('res.partner').search(cr, uid , [('codice_tributo','!=',None)] )
    
   
    _columns ={ 'partner_ids': fields.many2many('res.partner', string='Filtri per i partner',
                                         help="Solo i partner selezionati verranno stampati. "
                                              "Lasciare vuoto per stamparli tutti."),
               
               'estrai4' : fields.boolean('Estrai il 4% (cassa) dal codice 1040'),}
    _defaults = {
        'partner_ids': _get_partner_ids,
        'estrai4': False,
    }
    

    def pre_print_report(self, cr, uid, ids, data, context=None):
        data = super(account_print_cert_rit, self).pre_print_report(cr, uid, ids, data, context)
        if context is None:
            context = {}
         
        vals = self.read(cr, uid, ids,
                         ['partner_ids','fiscalyear_id'],
                         context=context)[0]
        data['ids'] = vals['partner_ids']

        
        return data

    def _print_report(self, cr, uid, ids, data, context=None):
        data = self.pre_print_report(cr, uid, ids, data, context=context)
        data['form']['estrai4'] = self.browse(cr, uid, ids, context=context)[0].estrai4

       
        return {'type': 'ir.actions.report.xml',
                'report_name': 'account_report_cert_rit_webkit',
                'datas': data,}

