from odoo import api, fields, models, SUPERUSER_ID
from odoo.tools.translate import _
from odoo.exceptions import UserError


class LmBusquedas(models.Model):
    _name = "tech.consumos.toa"
    _description = "TechMovil Seguimiento de Seriados"

    actividad = fields.Integer('1. Actividad')
    orden_trabajo = fields.Char('2. Orden Trab.  STL/TOA')
    tipo_tramite = fields.Char('3. Tipo Trámite')
    desc_tramite = fields.Char('4. Descrip. Trámite')
    tecnologia = fields.Char('5. Tecnología')
    material = fields.Integer('6. Material')
    desc_material = fields.Char('7. Descripción Material')
    num_serie = fields.Char('8. Número Serie', default='0')
    cantidad = fields.Integer('9. Cantidad')
    nim = fields.Char('10. Nim')
    estado = fields.Char('11. Estado')
    servicio = fields.Integer('12. Servicio')
    desc_servicio = fields.Char('13. Descripción Servicio')
    tecnico = fields.Char('14. Técnico')
    tipo_agrupador = fields.Char('15. Tipo de Agrupador')
    orden_compra = fields.Char('16. Orden de Compra')
    centro = fields.Char('17. Centro')
    desc_centro = fields.Char('18. Descripción Centro')
    almacen = fields.Char('19. Almacén')
    desc_almacen = fields.Char('20. Descripción Almacén')
    fecha_act_ofsc = fields.Char('21. Fecha Actividad OFSC')
    fecha_informado = fields.Char('22. Fecha Informado')
    fecha_ult_mod = fields.Char('23. Fecha última modificación')
    a_presup = fields.Integer('24. A.presup.')
    agrupador_pres_no = fields.Char('25. Agrupador de Pres MO')
    agrupador_pres_sm = fields.Char('26. Agrupador de Pres SM')
    almacen2 = fields.Char('27. Almacén')
    cantidad2 = fields.Integer('28. Cantidad')
    cege = fields.Char('29. CEGE')
    ceontro_contratista = fields.Char('30. Centro contratista')
    centro_coste = fields.Char('31. Centro coste')
    centr_servi = fields.Char('32. Centro Servicio')
    cl_valoracion = fields.Char('33. Cl.valoración')
    clase_movimiento = fields.Char('34. Clase de movimiento')
    contratista = fields.Integer('35. Contratista')
    contratista2 = fields.Char('36. Contratista')
    contrato_marco = fields.Char('37. Contrato Marco')
    costo_servicio = fields.Float('38. Costo del servicio', size=9, digits=(6, 3))
    deno_contrct = fields.Char('39. Denominación Contrat')
    desc_resultado = fields.Char('40. Descrip. Resultado')
    desc_almacen2 = fields.Char('41. Descripción Almacén')
    desc_centro2 = fields.Char('42. Descripción Centro ')
    desc_material2 = fields.Char('43. Descripción Material ')
    desc_servicio2 = fields.Char('44. Descripción Servicio ')
    doc_dev = fields.Char('45. Doc. Dev.')
    doc_material = fields.Char('46. Documento Material')
    doc_presup = fields.Integer('47. Documento Presup', size=11)
    elemento_pep = fields.Char('48. Elemento PEP')
    error = fields.Char('49 Error')
    estatus_act = fields.Char('50. Estatus de actividad')
    fecha_cance = fields.Char('51. Fecha Canc. Sal. Mer')
    fecha_cierre_act = fields.Char('52. Fecha Cierre Act.')
    fecha_ejer_sig = fields.Char('53. Fecha Ejercicio Sig.')
    fecha_inst = fields.Char('54. Fecha Instalación')
    fecha_mod = fields.Char('55. Fecha Modif.')
    hora_mod = fields.Char('56. Hora Modif.')
    id_sitio = fields.Char('57. ID de Sitio')
    importe_dev = fields.Float('58. Importe Dev', size=9, digits=(6, 3))
    importe_pep = fields.Float('59. Importe PEP', size=9, digits=(6, 3))
    ind_agrupa_presup = fields.Char('60. Ind Agrupador Presup')
    lote = fields.Char('61. Lote')
    material2 = fields.Integer('62. Material', size=9, digits=(9, 0))
    naturaleza_pep = fields.Char('63. Naturaleza PEP')
    nodo_region = fields.Char('64. Nodo Región')
    num_paso = fields.Integer('65. Número de Paso')
    num_posicion = fields.Integer('66. Número de Posición')
    num_serie2 = fields.Char('67. Número de serie')
    num_servicio = fields.Integer('68. Número servicio')
    operatoria = fields.Char('69. Operatoria')
    orden_trabajo2 = fields.Char('70. Orden de Trabajo')
    pais = fields.Char('71. País')
    pos_presup = fields.Char('72. Posición Presup')
    prec_med_var_cal = fields.Float('73. Prec med var Cal', size=9, digits=(4, 5))
    pre_med_var = fields.Float('74. Precio Medio var', size=9, digits=(4, 5))
    proce = fields.Char('75. Procesado')
    provincia = fields.Char('76. Provincia')
    resultado = fields.Integer('77. Resultado')
    sist_legado = fields.Boolean('78. Sistema Legado')
    sociedad_fi = fields.Char('79. Sociedad FI')
    tecnologia2 = fields.Char('80. Tecnologia')
    tipo_tramite2 = fields.Char('81. Tipo trámite')
    tramite_sin_serie = fields.Char('82. Tramite sin Serie')
    ubic_tecn = fields.Char('83. Ubic.técn.')
    unidad_org = fields.Integer('84. Unidad org.')
    usuario = fields.Char('85. Usuario')
    usu_cancela = fields.Char('86. Usuario Cancela S')
    usu_cierre_act = fields.Char('87. Usuario cierre act')
    usu_eje_s = fields.Char('88. Usuario Ejercicio S')
    usu_mod = fields.Char('89. Usuario Modificación')
    

#    <--------------- Crea la funcion del Trigger - -------------------- ->
#
#CREATE FUNCTION toa_actu() returns trigger
#as
#$$
#
#begin
#
#UPDATE tech_stock_seriado SET  estado_uso = 'usado' WHERE num_serie = new.num_serie
#
#return new
#End
#$$
#language plpgsql
#
#<-----------------Crea el Trigger - ------------------------------ ->
#create trigger tr_consumos_toa1 after Insert on tech_consumos_toa
#for each row
#execute procedure toa_actu()