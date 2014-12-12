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

from osv import fields, osv


class partner(osv.osv):

    _inherit = "res.partner"
    _description = "Genio la fenice gestione lettera intento"
   
    _columns = {
         #esenzione iva
        'dichiarazione_esenzione_iva': fields.integer('Nr.Dich.esenzione IVA cliente',help="Numero dichiarazione esenzione IVA del cliente"),
        'protocollo_dichiarazione_esenzione_iva': fields.integer('Protocollo interno esenzione IVA',help="Numero di protocollo interno per la registrazione della dichiarazione di esenzione IVA"),
        'data_dichiarazione_esenzione_iva': fields.date('Data dichiarazione', help="Data della dichiarazione del cliente per l'esenzione IVA"),
        'data_protocollo_interno_esenzione_iva': fields.date('Data protocollo interno', help="Data del protocollo interno per la registrazione della dichiarazione di esenzione IVA"),
         
    }
    
partner()



class account_invoice(osv.osv):
    _inherit = "account.invoice"
    #creazione diretta fattura

    def onchange_partner_id(self, cr, uid, ids, type, partner_id,date_invoice=False, payment_term=False, partner_bank_id=False, company_id=False):
        if not partner_id:
            return {'value': {
            'account_id': False,
            'payment_term': False,
            }
        }
            
        result =  super(account_invoice, self).onchange_partner_id(cr, uid, ids, type, partner_id,date_invoice=date_invoice, payment_term=payment_term,partner_bank_id=partner_bank_id, company_id=company_id)
        valori=result.get('value',{})
        
        partner = self.pool.get('res.partner').browse(cr, uid, partner_id)
        if partner.dichiarazione_esenzione_iva:
            valori['dichiarazione_esenzione_iva']=partner.dichiarazione_esenzione_iva
        if partner.protocollo_dichiarazione_esenzione_iva:    
            valori['protocollo_dichiarazione_esenzione_iva']=partner.protocollo_dichiarazione_esenzione_iva
        if partner.data_dichiarazione_esenzione_iva:
            valori['data_dichiarazione_esenzione_iva']=partner.data_dichiarazione_esenzione_iva
        if partner.data_protocollo_interno_esenzione_iva:
            valori['data_protocollo_interno_esenzione_iva']=partner.data_protocollo_interno_esenzione_iva

        
        return {'value': valori}
        
    
    _columns = {'dichiarazione_esenzione_iva': fields.integer('Nr.Dich.esenzione IVA cliente',help="Numero dichiarazione esenzione IVA del cliente"),
                'protocollo_dichiarazione_esenzione_iva': fields.integer('Protocollo interno esenzione IVA',help="Numero di protocollo interno per la registrazione della dichiarazione di esenzione IVA"),
                'data_dichiarazione_esenzione_iva': fields.date('Data dichiarazione', help="Data della dichiarazione del cliente per l'esenzione IVA"),
                'data_protocollo_interno_esenzione_iva': fields.date('Data protocollo interno', help="Data del protocollo interno per la registrazione della dichiarazione di esenzione IVA"),
                }


account_invoice()


class stock_picking(osv.osv):
    #fatturazione da ordine di consegna
    _inherit = "stock.picking"

    def action_invoice_create(self, cr, uid, ids, journal_id=False, group=False, type='out_invoice', context=None):
        res=super(stock_picking, self).action_invoice_create(cr, uid, ids, journal_id=False, group=False, type='out_invoice', context=None)
        
        for id_invoice in res.values():
            invoice = self.pool.get('account.invoice').browse(cr, uid, id_invoice)
            
            dichiarazione_esenzione_iva=''
            protocollo_dichiarazione_esenzione_iva=''
            data_dichiarazione_esenzione_iva=''
            data_protocollo_interno_esenzione_iva=''
            
            partner = invoice.partner_id
           
            if partner.dichiarazione_esenzione_iva:
                dichiarazione_esenzione_iva=partner.dichiarazione_esenzione_iva
            if partner.protocollo_dichiarazione_esenzione_iva:    
                protocollo_dichiarazione_esenzione_iva=partner.protocollo_dichiarazione_esenzione_iva
            if partner.data_dichiarazione_esenzione_iva:
                data_dichiarazione_esenzione_iva=partner.data_dichiarazione_esenzione_iva
            if partner.data_protocollo_interno_esenzione_iva:
                data_protocollo_interno_esenzione_iva=partner.data_protocollo_interno_esenzione_iva
    
            invoice.write({'dichiarazione_esenzione_iva': dichiarazione_esenzione_iva,'protocollo_dichiarazione_esenzione_iva': protocollo_dichiarazione_esenzione_iva,'data_dichiarazione_esenzione_iva':data_dichiarazione_esenzione_iva,'data_protocollo_interno_esenzione_iva':data_protocollo_interno_esenzione_iva})
            
        return res
  
stock_picking()         


class sale_order(osv.osv):
    _inherit = "sale.order"
    #fatturazione da ordine di vendita
    
    def _prepare_invoice(self, cr, uid, order, lines, context=None):
        invoice_vals=super(sale_order, self)._prepare_invoice( cr, uid, order, lines, context=None)
        
        partner = self.pool.get('res.partner').browse(cr, uid, invoice_vals['partner_id'])

        if partner.dichiarazione_esenzione_iva:
            invoice_vals['dichiarazione_esenzione_iva']=partner.dichiarazione_esenzione_iva
        if partner.protocollo_dichiarazione_esenzione_iva:    
            invoice_vals['protocollo_dichiarazione_esenzione_iva']=partner.protocollo_dichiarazione_esenzione_iva
        if partner.data_dichiarazione_esenzione_iva:
            invoice_vals['data_dichiarazione_esenzione_iva']=partner.data_dichiarazione_esenzione_iva
        if partner.data_protocollo_interno_esenzione_iva:
            invoice_vals['data_protocollo_interno_esenzione_iva']=partner.data_protocollo_interno_esenzione_iva
        
   
        return invoice_vals
       

sale_order()