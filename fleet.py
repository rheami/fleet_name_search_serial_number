# -*- coding: utf-8 -*-
# © 2018 Michel Rheault
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, api


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'


    @api.model
    def on_install(self):
        """ on install add vin_sn field in name_search_ids to search vehicle by vin_sn """
        vin_sn_field = self.env.ref('fleet.field_fleet_vehicle_vin_sn')
        model = self.env.ref('fleet.model_fleet_vehicle')
        model.name_search_ids = vin_sn_field
