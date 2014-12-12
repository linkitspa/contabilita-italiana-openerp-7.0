# -*- coding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) 2012 Andrea Cometa.
#    Email: info@andreacometa.it
#    Web site: http://www.andreacometa.it
#    Copyright (C) 2012 Agile Business Group sagl (<http://www.agilebg.com>)
#    Copyright (C) 2012 Domsense srl (<http://www.domsense.com>)
#    Copyright (C) 2012 Associazione OpenERP Italia
#    (<http://www.openerp-italia.org>).
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
import decimal_precision as dp

class certificazioneritenute_configurazione(osv.osv):
    
    _name = "certificazioneritenute.configurazione"
    _description = "Configurazione codici tributo per certificazione ritenute"

    _columns = {
        'name' : fields.char("Codice",required=True),
        'desc' : fields.char("Descrizione", size=64, required=True),
        'aliquota' : fields.float('% Aliquota', required=True,digits_compute=dp.get_precision('Account')),
        'aliquota_imponibile' : fields.float('% Aliquota imponibile', required=True),  
                 
    }

    _defaults = {
        'aliquota_imponibile': 100,
    }
    
   
certificazioneritenute_configurazione()

