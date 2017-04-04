# -*- coding:utf-8 -*-
from odoo import api, SUPERUSER_ID


def _entrepot_nb(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
#    warehouses = env['stock.warehouse'].search([('active','=',1)])
    # correction des noms auto-généré pour les stock.location, si erronné
    warehouse = env['stock.warehouse'].search([('code','=', 'SENB')], limit=1)
    
    location = env['stock.location'].search([('name','=','Pesée'),('location_id','=',warehouse.lot_stock_id.id)], limit=1)

    if not location:
        vals = {
            'name': 'Pesée',
            'location_id' : warehouse.lot_stock_id.id,
            'usage' : 'internal',
            'maxItem' :250,
            }
        env['stock.location'].create(vals)    

    location = env['stock.location'].search([('name','=','Classement'),('location_id','=',warehouse.lot_stock_id.id)], limit=1)

    if not location:
        vals = {
            'name': 'Classement',
            'location_id' : warehouse.lot_stock_id.id,
            'usage' : 'internal',
            'maxItem' :250,
            }
        env['stock.location'].create(vals)    


def _setup_maple(cr, registry):
    #write the default debit account on salary rule having xml_id like 'l10n_be_hr_payroll.1' up to 'l10n_be_hr_payroll.1409'

    _entrepot_nb(cr, registry)