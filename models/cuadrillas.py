from odoo import api, fields, models, SUPERUSER_ID
from odoo.tools.translate import _
from odoo.exceptions import UserError

class cuadrillas(models.Model):
    _name = "tech.cuadrillas"
    _description = "TechMovil Cuadrillas"
    
    nombre_cuadrilla=fields.Char('Nombre de la cuadrilla', required=True)
    tecnico_cuadrilla=fields.Char('Tecnico de la cuadrilla', required=True)
    ubicacion_cuadrilla=fields.Selection(
        [('Rosario', 'Rosario'),
         ('Buenos Aires', 'Buenos Aires')],
        'Ubicacion de la Cuadrilla', default='Buenos Aires', required=True)