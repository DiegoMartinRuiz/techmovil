from odoo import api, fields, models, SUPERUSER_ID
from odoo.tools.translate import _
from odoo.exceptions import UserError


class stock_no_seriado(models.Model):
    _name = "tech.stock.no.seriado"
    _description = "TechMovil Stok No Seriados"
    
    contratista=fields.Char('Contratista')
    raz_social=fields.Char('Razón Social')
    cod_opera=fields.Char('Código de Operatoria')
    centro=fields.Char('Centro')
    sociedad=fields.Char('Sociedad')
    almacen=fields.Char('Almacén')
    num_material=fields.Char('Número de Material')
    desc_material=fields.Char('Descripción de Material')
    elemento_pep=fields.Char('Elemento PEP')
    lote=fields.Char('Lote')
    cantidad=fields.Integer('Cantidad')
    unidad=fields.Char('Unidad')
    estado=fields.Char('Estado')
    comprometido_orden=fields.Integer('Comprometido en Ordenes')
    disponible=fields.Integer('Disponible')
    asig_almacen=fields.Char('Almacen al que se asigno')
    estado_uso=fields.Char('El producto esta disponible para ser Utilizado')