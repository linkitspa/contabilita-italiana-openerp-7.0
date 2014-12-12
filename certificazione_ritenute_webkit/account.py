# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2011-2012 Associazione OpenERP Italia
#    (<http://www.openerp-italia.org>).
#    Copyright (C) 2012 Agile Business Group sagl (<http://www.agilebg.com>)
#    Copyright (C) 2012 Domsense srl (<http://www.domsense.com>)
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
from tools.translate import _

class account_account(osv.osv):
    # flag CEE per stampa sui registri
    _inherit =  "account.account"
    
    _columns = {
        'no_rit' : fields.boolean('Report certificazioni: conto non soggetto a ritenuta'),
        'cassa_previdenza' : fields.boolean('Report certificazioni: conto totalizzato nella cassa previdenza'),
     }
    _defaults = {
        'no_rit': False,
        'cassa_previdenza': False,
    }
account_account()

