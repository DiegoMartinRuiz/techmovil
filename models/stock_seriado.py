from odoo import api, fields, models, SUPERUSER_ID
from odoo.tools.translate import _
from odoo.exceptions import UserError
from datetime import datetime
from odoo import tools
from dateutil.relativedelta import relativedelta
from datetime import timedelta

class LmBusquedas(models.Model):
     _name = "tech.stock.seriado"
     _description = "TechMovil Stok Seriados"
  
     
     contratista=fields.Char('Contratista')
     raz_social=fields.Char('Razón Social')
     cod_opera=fields.Char('Código de Operatoria')
     centro=fields.Char('Centro')
     sociedad=fields.Char('Sociedad')
     almacen=fields.Char('Almacén')
     num_material=fields.Char('Número de Material')
     desc_material=fields.Char('Descripción de Material')
     num_serie=fields.Char('Número de Serie')
     mac_address=fields.Char('MAC Addres')
     elemento_pep=fields.Char('Elemento PEP')
     lote=fields.Char('Lote')
     cantidad=fields.Integer('Cantidad')
     unidad=fields.Char('Unidad')
     estado=fields.Char('Estado')
     fecha_ingreso=fields.Date('Fecha Ingreso')
     pedido=fields.Char('Pedido')
     fecha_ult_mov=fields.Char('Fec. Ult Mov')
     cl_mov=fields.Char('Cl. Mov.')
     doc_mat=fields.Char('Doc. Mat.')
     orden=fields.Char('Orden')
     posicion=fields.Integer('Posición')
     documento_material=fields.Char('Documento Material')
     rechazado=fields.Char('Rechazado')
     pre_aprobdo=fields.Char('Pre Aprobado')
     aprobado=fields.Char('Aprobado')
     asig_almacen=fields.Char('Almacen al que se asigno')
     estado_uso=fields.Char('El producto esta disponible para ser Utilizado', default='Disponible')
     _sql_constraints = [
    ('num_serie_unique', 'unique(num_serie)', 'El numero de serie ya existe')
      ]
     @api.depends('fecha_ingreso')
     def fecha_caducidad_fun(self):
        self.fecha_caducidad=self.fecha_ingreso+relativedelta(days=120)

     fecha_caducidad=fields.Date('Fecha de Caducidad', compute='fecha_caducidad_fun', store=True)