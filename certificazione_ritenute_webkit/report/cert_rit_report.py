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


from datetime import datetime

from openerp import pooler
from openerp.report import report_sxw
from openerp.tools.translate import _
import time
from openerp import tools
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT

class cert_report_webkit(report_sxw.rml_parse):

    def __init__(self, cursor, uid, name, context):
        super(cert_report_webkit, self).__init__(cursor, uid, name,  context=context)
        self.pool = pooler.get_pool(self.cr.dbname)
        self.cursor = self.cr
        
        tomorrow = datetime.today() 
        
        footer_date=tomorrow.strftime(DEFAULT_SERVER_DATE_FORMAT)
        self.localcontext.update({
            'cr': cursor,
            'uid': uid,
            'footer_date':footer_date,
            'lines': self.get_lines,
            'report_name': 'Dettaglio ore',
        })


    def get_lines(self, partner_id):
        item = {} 
        res=[]
        
        Compenso_lordo=0
        IVA=0
        Somme_n_sogg=0
        Cassa_prev=0
        Imponibile=0
        Rit_operata=0
        Rit_sospesa=0
        Provv_n_sogg=0
        
        date_start = self.localcontext['start_period'].date_start
        date_stop = self.localcontext['stop_period'].date_stop
        estrai4 = self.localcontext['estrai4']
        
        account_invoice = self.pool.get('account.invoice')
        res_partner = self.pool.get('res.partner')
        #****aggiungere la selezione per anno
        
        
        #recupero gli indirizzi di fatturazione
        lista_ids_fatt=[]
        lista_ids_fatt.append(partner_id.id)
        obj_indirizzi = res_partner.search(self.cr, self.uid, [('parent_id', 'in', [partner_id.id]),('type','=','invoice')])
        if obj_indirizzi:
           for indirizzo in obj_indirizzi:
              lista_ids_fatt.append(indirizzo)
        
        obj_invoice = account_invoice.search(self.cr, self.uid, [('partner_id', 'in', lista_ids_fatt),
                                                                 ('type', '=', 'in_invoice'),
                                                                 ('state', '=', 'paid'),
                                                                 #('has_withholding', 'is',True),
                                                                 ('withholding_amount', '>',0),
                                                                 ('registration_date', '>=', date_start),
                                                                 ('registration_date', '<=', date_stop)]                                                                 )
        if obj_invoice:
           #ciclo su tutte le fatture trovate
           for invoice in obj_invoice: 
               invoice_doc=account_invoice.browse(self.cr, self.uid, invoice)
              
               for line in invoice_doc.invoice_line:
                   # somma totale righe soggette a ritenuta
                   Compenso_lordo += line.price_subtotal
                   if line.account_id.no_rit:
                       Somme_n_sogg += line.price_subtotal
                       
                   # somma totale righe di tipo cassa
                   if line.account_id.cassa_previdenza:
                       Cassa_prev += line.price_subtotal   
                        
               IVA += invoice_doc.amount_tax
               Rit_operata += invoice_doc.withholding_amount
          
           
           if partner_id.codice_tributo.aliquota_imponibile and partner_id.codice_tributo.aliquota_imponibile !=0 :
              perc=partner_id.codice_tributo.aliquota_imponibile/100
              Imponibile = ( Compenso_lordo - Somme_n_sogg )* perc
           elif partner_id.codice_tributo.aliquota_imponibile and partner_id.codice_tributo.aliquota_imponibile ==100 :
               Imponibile = Compenso_lordo - Somme_n_sogg    
           else:
               Imponibile =  0   
                                                   
           Provv_n_sogg += ( Compenso_lordo - Somme_n_sogg ) - Imponibile
           if estrai4 and partner_id.codice_tributo.name=='1040':
               Cassa_prev=(Imponibile / 1.04 ) * 0.04
               Imponibile=Imponibile-Cassa_prev
       
        item = {'Compenso_lordo':Compenso_lordo,
                'IVA': IVA,
                'Somme_n_sogg': Somme_n_sogg,
                'Cassa_prev':Cassa_prev,
                'Imponibile': Imponibile,
                'Rit_operata': Rit_operata,
                'Rit_sospesa': Rit_sospesa,
                'Provv_n_sogg': Provv_n_sogg,
         }
        res.append(item) 
             
        return res
 
    
    def get_first_fiscalyear_period(self, fiscalyear):
        return self._get_st_fiscalyear_period(fiscalyear)

    def get_last_fiscalyear_period(self, fiscalyear):
        return self._get_st_fiscalyear_period(fiscalyear, order='DESC')

    def _get_st_fiscalyear_period(self, fiscalyear, special=False, order='ASC'):
        period_obj = self.pool.get('account.period')
        p_id = period_obj.search(self.cursor,
                                 self.uid,
                                 [('fiscalyear_id', '=', fiscalyear.id)],
                                 limit=1,
                                 order='date_start %s' % (order,))
        if not p_id:
            raise osv.except_osv(_('No period found'), '')
        return period_obj.browse(self.cursor, self.uid, p_id[0])
    
    def set_context(self, objects, data, ids, report_type=None):
        
        anno = self.pool.get('account.fiscalyear').browse(self.cr, self.uid, [data['form'].get('fiscalyear_id')], context=None)[0].code
        fiscalyear = self.pool.get('account.fiscalyear').browse(self.cr, self.uid, [data['form'].get('fiscalyear_id')], context=None)[0]
        
        if fiscalyear:
            start_period = self.get_first_fiscalyear_period(fiscalyear)
            stop_period = self.get_last_fiscalyear_period(fiscalyear)

      
        estrai4=data['form'].get('estrai4')
        
        self.localcontext.update({
            'anno': anno,
            'start_period': start_period,
            'stop_period': stop_period,
            'estrai4':estrai4,
            })
      
        return super(cert_report_webkit, self).set_context(objects, data, ids, report_type=report_type)


  
report_sxw.report_sxw('report.account_report_cert_rit_webkit',
                             'res.partner',
                             'addons/certificazione_ritenute_webkit/report/templates/cert_rit_report.mako',
                             parser=cert_report_webkit)
