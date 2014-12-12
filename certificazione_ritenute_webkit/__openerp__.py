# -*- coding: utf-8 -*-
##############################################################################
#
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
{
    'name': 'Genio la fenice certificazioni ritenute webkit',
    'description': '',
    'version': '1.0',
    'category': 'Finance',
    'description': """\
        -compilare la tabella con i codici tributo in contablità configurazione 
        -compilare data e luogo di nascita sull'anagrafica fornitore
        -compilare nei dati azienda il campo registro imprese, R.E.A. e capitale sociale
        -indicare i conti del piano dei conti che sono esclusi dall'imponibile ritenute
        -indicare i conti del piano dei conti che sono inclusi nella cassa prev.""",
    'images': [],
    'depends': ['account',
                'report_webkit',
                ],
    'demo' : [],
    
    'data': [      
                   'data/hr_cert_rit_header.xml',
                   'report/report.xml',
                   'wizard/cert_rit_wizard.xml',
                   'report_menus.xml',
                   'account_view.xml',
                   'partner_view.xml',
                   'company_view.xml',
                   'configurazione_view.xml',
                   'security/access_rule.xml',
                   'security/ir.model.access.csv',
                   ],        
    'update_xml': ['security/access_rule.xml'],                   
    'active': False,
    'installable': True,
    'application': True,
}
