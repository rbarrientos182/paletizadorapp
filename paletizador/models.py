# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Armadotarimas(models.Model):
    idarmadotarimas = models.AutoField(db_column='idArmadoTarimas', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField()
    iddeposito = models.IntegerField()
    idruta = models.IntegerField()
    numerotarima = models.IntegerField()
    tipotarima = models.CharField(max_length=45)
    cajas_tarima = models.FloatField()
    secuencia_sku = models.IntegerField()
    sku = models.IntegerField()
    cajas_sku = models.FloatField()
    complemento = models.CharField(max_length=45, blank=True, null=True)
    acomodo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'armadotarimas'


class Cambiosmotivos(models.Model):
    idcambiosmotivos = models.AutoField(db_column='idCambiosMotivos', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    agrupador = models.CharField(max_length=45, blank=True, null=True)
    arearesponsable = models.CharField(max_length=45, blank=True, null=True)
    areaimpactar = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cambiosmotivos'


class Capturacambios(models.Model):
    idcambios = models.AutoField(primary_key=True)
    idoperacion = models.ForeignKey('Operaciones', models.DO_NOTHING, db_column='idoperacion')
    numempleado = models.ForeignKey('Usrcambios', models.DO_NOTHING, db_column='NumEmpleado')  # Field name made lowercase.
    idcambiosmotivos = models.ForeignKey(Cambiosmotivos, models.DO_NOTHING, db_column='idCambiosMotivos')  # Field name made lowercase.
    idproductocambio = models.ForeignKey('Productoscambios', models.DO_NOTHING, db_column='idProductoCambio')  # Field name made lowercase.
    nud = models.IntegerField()
    fechacambio = models.DateField(db_column='FechaCambio')  # Field name made lowercase.
    cantidad = models.IntegerField()
    idruta = models.IntegerField(blank=True, null=True)
    estatusdis = models.IntegerField(db_column='estatusDis', blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.DateField(db_column='fechaEntrega', blank=True, null=True)  # Field name made lowercase.
    horacaptura = models.DateTimeField(db_column='horaCaptura', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'capturacambios'


class CatalogoIncidencia(models.Model):
    idcatalogo_incidencia = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'catalogo_incidencia'


class Cierre(models.Model):
    idcierre = models.AutoField(primary_key=True)
    idoperacion = models.IntegerField()
    estatus = models.IntegerField(blank=True, null=True)
    fechaoperacion = models.DateField(db_column='fechaOperacion', blank=True, null=True)  # Field name made lowercase.
    estatusdis = models.IntegerField(db_column='estatusDis', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cierre'


class Clientes(models.Model):
    nud = models.IntegerField()
    ppp = models.IntegerField(blank=True, null=True)
    vpp = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=125, blank=True, null=True)
    direccion = models.CharField(max_length=125, blank=True, null=True)
    calleizq = models.CharField(max_length=125, blank=True, null=True)
    calleder = models.CharField(max_length=125, blank=True, null=True)
    localidad = models.CharField(max_length=125, blank=True, null=True)
    municipio = models.CharField(max_length=125, blank=True, null=True)
    colonia = models.CharField(max_length=125, blank=True, null=True)
    vacia = models.CharField(max_length=10, blank=True, null=True)
    cp = models.IntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=25, blank=True, null=True)
    giro = models.IntegerField(blank=True, null=True)
    categoria = models.CharField(max_length=2, blank=True, null=True)
    volpromsem = models.IntegerField(db_column='volPromSem', blank=True, null=True)  # Field name made lowercase.
    tipofrecuencia = models.CharField(db_column='tipoFrecuencia', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dia = models.CharField(max_length=7, blank=True, null=True)
    frecuencia = models.IntegerField(blank=True, null=True)
    iddeposito = models.IntegerField()
    concatena = models.CharField(max_length=125, blank=True, null=True)
    f1 = models.IntegerField(blank=True, null=True)
    f2 = models.IntegerField(blank=True, null=True)
    latitud = models.CharField(max_length=45, blank=True, null=True)
    longitud = models.CharField(max_length=45, blank=True, null=True)
    alta = models.CharField(max_length=45, blank=True, null=True)
    volacum = models.IntegerField(db_column='volAcum', blank=True, null=True)  # Field name made lowercase.
    semanas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'
        unique_together = (('nud', 'iddeposito'),)


class Contactos(models.Model):
    idcontactos = models.AutoField(primary_key=True)
    iddeposito = models.ForeignKey('Deposito', models.DO_NOTHING, db_column='idDeposito')  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    email = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contactos'


class Deposito(models.Model):
    iddeposito = models.IntegerField(db_column='idDeposito', primary_key=True)  # Field name made lowercase.
    idzona = models.ForeignKey('Zona', models.DO_NOTHING, db_column='idZona')  # Field name made lowercase.
    deposito = models.CharField(max_length=30)
    latitud = models.CharField(max_length=15, blank=True, null=True)
    longitud = models.CharField(max_length=15, blank=True, null=True)
    gerentedeposito = models.CharField(db_column='gerenteDeposito', max_length=45, blank=True, null=True)  # Field name made lowercase.
    jefeentrega = models.CharField(db_column='jefeEntrega', max_length=45, blank=True, null=True)  # Field name made lowercase.
    operadorsistema = models.CharField(db_column='operadorSistema', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telefonoext = models.CharField(db_column='telefonoExt', max_length=45, blank=True, null=True)  # Field name made lowercase.
    correogd = models.CharField(db_column='correoGD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    correoje = models.CharField(db_column='correoJE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    correoop = models.CharField(db_column='correoOP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estatus = models.IntegerField(blank=True, null=True)
    total_vpp = models.IntegerField(blank=True, null=True)
    total_ppp = models.IntegerField(blank=True, null=True)
    total_av = models.IntegerField(blank=True, null=True)
    diferenciahoraria = models.IntegerField(db_column='diferenciaHoraria', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deposito'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Empaque(models.Model):
    idempaque = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'empaque'


class Familia(models.Model):
    idfamilia = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'familia'


class Gruposupervision(models.Model):
    idgruposupervision = models.AutoField(primary_key=True)
    idoperacion = models.ForeignKey('Operaciones', models.DO_NOTHING, db_column='idoperacion')
    numgrupo = models.IntegerField(blank=True, null=True)
    numempleado = models.CharField(db_column='NumEmpleado', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gruposupervision'


class Horariotablero(models.Model):
    iddeposito = models.IntegerField(db_column='idDeposito')  # Field name made lowercase.
    idruta = models.IntegerField(db_column='idRuta')  # Field name made lowercase.
    salida = models.TimeField()
    llegada = models.TimeField()

    class Meta:
        managed = False
        db_table = 'horariotablero'
        unique_together = (('iddeposito', 'idruta'),)


class Incidencias(models.Model):
    idincidencias = models.AutoField()
    idcatalogo_incidencia = models.ForeignKey(CatalogoIncidencia, models.DO_NOTHING, db_column='idcatalogo_incidencia')
    fecha = models.DateField()
    iddeposito = models.IntegerField()
    semana = models.IntegerField()
    ruta = models.IntegerField()
    comentarios = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incidencias'
        unique_together = (('idincidencias', 'idcatalogo_incidencia'),)


class KmFijos(models.Model):
    idkm_fijos = models.AutoField(primary_key=True)
    no_deposito = models.IntegerField()
    ruta = models.IntegerField()
    dia = models.CharField(max_length=45)
    kmtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tiporuta = models.IntegerField(db_column='tipoRuta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'km_fijos'


class Logcambios(models.Model):
    idlog = models.AutoField(primary_key=True)
    numempleado = models.ForeignKey('Usrcambios', models.DO_NOTHING, db_column='NumEmpleado')  # Field name made lowercase.
    iidoperacion = models.ForeignKey('Usrcambios', models.DO_NOTHING, db_column='iidoperacion')
    fechahora = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'logcambios'


class Marca(models.Model):
    idmarca = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'marca'


class Notificador(models.Model):
    idnotificador = models.AutoField(primary_key=True)
    iddeposito = models.ForeignKey(Deposito, models.DO_NOTHING, db_column='idDeposito')  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    ip = models.CharField(max_length=45, blank=True, null=True)
    puerto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificador'


class Operaciones(models.Model):
    idoperacion = models.AutoField(primary_key=True)
    iddeposito = models.ForeignKey(Deposito, models.DO_NOTHING, db_column='idDeposito')  # Field name made lowercase.
    mercado = models.IntegerField()
    coordinador_despacho = models.CharField(max_length=150)
    nocelda = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operaciones'


class Orden(models.Model):
    fecha = models.DateField()
    idruta = models.IntegerField(db_column='idRuta')  # Field name made lowercase.
    idoperacion = models.IntegerField()
    nud = models.IntegerField()
    secuencia = models.IntegerField(blank=True, null=True)
    csio = models.IntegerField(blank=True, null=True)
    cfisicas = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cequivalentes = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    km = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_preventa = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden'
        unique_together = (('fecha', 'idruta', 'idoperacion', 'nud'),)


class OrdenConcentrado(models.Model):
    fecha = models.DateField()
    idruta = models.IntegerField()
    idoperacion = models.IntegerField()
    ctesprog = models.IntegerField(blank=True, null=True)
    csio = models.IntegerField(blank=True, null=True)
    cfisicas = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cequivalentes = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    km = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_preventa = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_concentrado'
        unique_together = (('fecha', 'idruta', 'idoperacion'),)


class OrdenDetalle(models.Model):
    fecha = models.DateField()
    idruta = models.IntegerField(db_column='idRuta')  # Field name made lowercase.
    idoperacion = models.IntegerField()
    nud = models.IntegerField()
    sku = models.IntegerField()
    csio = models.IntegerField()
    cgepp = models.DecimalField(max_digits=10, decimal_places=2)
    clavebodega = models.IntegerField()
    secuencia = models.IntegerField()
    rutatransaccion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orden_detalle'
        unique_together = (('fecha', 'idruta', 'idoperacion', 'nud', 'sku'),)


class OrdenDetalleT27(models.Model):
    fecha = models.DateField()
    idruta = models.IntegerField(db_column='idRuta')  # Field name made lowercase.
    sku = models.IntegerField()
    csio = models.IntegerField(blank=True, null=True)
    cgepp = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'orden_detalle_t27'
        unique_together = (('fecha', 'idruta', 'sku'),)


class OrdenDetalleT27Grb(models.Model):
    fecha = models.DateField()
    idruta = models.IntegerField(db_column='idRuta')  # Field name made lowercase.
    sku = models.IntegerField()
    csio = models.IntegerField(blank=True, null=True)
    cgepp = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'orden_detalle_t27_grb'
        unique_together = (('fecha', 'idruta', 'sku'),)


class OrdenDetalleTemp(models.Model):
    fecha = models.DateField()
    idruta = models.IntegerField(db_column='idRuta')  # Field name made lowercase.
    sku = models.IntegerField()
    csio = models.IntegerField(blank=True, null=True)
    cgepp = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'orden_detalle_temp'
        unique_together = (('fecha', 'idruta', 'sku'),)


class Paletizador(models.Model):
    idpaletizador = models.AutoField(primary_key=True)
    iddeposito = models.IntegerField(unique=True)
    largotarima = models.IntegerField()
    anchotarima = models.IntegerField(blank=True, null=True)
    margen = models.IntegerField()
    margen1 = models.IntegerField(blank=True, null=True)
    tipotarima1 = models.CharField(max_length=45, blank=True, null=True)
    tipotarima2 = models.CharField(max_length=45, blank=True, null=True)
    tipotarima3 = models.CharField(max_length=45, blank=True, null=True)
    tipotarima4 = models.CharField(max_length=45, blank=True, null=True)
    tipotarima5 = models.CharField(max_length=45, blank=True, null=True)
    porcentaje_completa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    porcentaje_bandera = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    porcentaje_escuadra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    porcentaje_combinada = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sku_garrafon = models.CharField(max_length=60, blank=True, null=True)
    calculo_x_pasillos = models.IntegerField(db_column='Calculo_X_Pasillos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paletizador'


class PaletizadorLog(models.Model):
    idpaletizador_log = models.AutoField(db_column='idPaletizador_Log')  # Field name made lowercase.
    iddeposito = models.IntegerField(db_column='Iddeposito')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    inicio = models.TimeField(db_column='Inicio', blank=True, null=True)  # Field name made lowercase.
    fin = models.TimeField(db_column='Fin', blank=True, null=True)  # Field name made lowercase.
    estatus = models.IntegerField(db_column='Estatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paletizador_log'
        unique_together = (('idpaletizador_log', 'iddeposito'),)


class Paquete(models.Model):
    idpaquete = models.AutoField(primary_key=True)
    paquete = models.CharField(max_length=45)
    altura = models.FloatField(blank=True, null=True)
    ancho = models.FloatField(blank=True, null=True)
    profundidad = models.FloatField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    equivalencia = models.FloatField(blank=True, null=True)
    cajasxcapa = models.IntegerField(blank=True, null=True)
    capasxtarima = models.IntegerField(blank=True, null=True)
    totalcajas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paquete'


class Pasillos(models.Model):
    idpasillos = models.IntegerField(db_column='idPasillos', primary_key=True)  # Field name made lowercase.
    iddeposito = models.IntegerField()
    idpasillo = models.IntegerField(db_column='IdPasillo')  # Field name made lowercase.
    idpaquete = models.IntegerField(db_column='IdPaquete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pasillos'


class Permisos(models.Model):
    idusuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idUsuarios')  # Field name made lowercase.
    idoperacion = models.ForeignKey('Operaciones', models.DO_NOTHING, db_column='idoperacion')

    class Meta:
        managed = False
        db_table = 'permisos'
        unique_together = (('idusuarios', 'idoperacion'),)


class Poligonos(models.Model):
    idpoligonos = models.AutoField(primary_key=True)
    hemisferio = models.IntegerField()
    idruta = models.IntegerField(db_column='idRuta')  # Field name made lowercase.
    idoperacion = models.IntegerField()
    longitud = models.CharField(db_column='Longitud', max_length=15, blank=True, null=True)  # Field name made lowercase.
    latitud = models.CharField(db_column='Latitud', max_length=15, blank=True, null=True)  # Field name made lowercase.
    secuencia = models.IntegerField(blank=True, null=True)
    centro_latitud = models.CharField(max_length=15, blank=True, null=True)
    centro_longitud = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poligonos'


class Presentacion(models.Model):
    idpresentacion = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'presentacion'


class Procesaorden(models.Model):
    nombrearchivo = models.CharField(db_column='NombreArchivo', primary_key=True, max_length=45)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'procesaorden'


class Productos(models.Model):
    sku = models.IntegerField(primary_key=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=85)  # Field name made lowercase.
    idmarca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='idmarca')
    idfamilia = models.ForeignKey(Familia, models.DO_NOTHING, db_column='idfamilia')
    idsabor = models.ForeignKey('Sabor', models.DO_NOTHING, db_column='idsabor')
    idsegmento = models.ForeignKey('Segmento', models.DO_NOTHING, db_column='idsegmento')
    idpresentacion = models.ForeignKey(Presentacion, models.DO_NOTHING, db_column='idpresentacion')
    idpaquete = models.ForeignKey(Paquete, models.DO_NOTHING, db_column='idpaquete')
    cavidades = models.IntegerField(blank=True, null=True)
    serv = models.CharField(max_length=45, blank=True, null=True)
    conversioncf = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class Productoscambios(models.Model):
    idproductocambio = models.AutoField(db_column='idProductoCambio')  # Field name made lowercase.
    idoperacion = models.ForeignKey(Operaciones, models.DO_NOTHING, db_column='idoperacion')
    sku = models.IntegerField()
    descripcioninterna = models.CharField(db_column='DescripcionInterna', max_length=125)  # Field name made lowercase.
    skuconver = models.IntegerField(db_column='skuConver', blank=True, null=True)  # Field name made lowercase.
    estatus = models.IntegerField(blank=True, null=True)
    tmercado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'productoscambios'
        unique_together = (('idproductocambio', 'idoperacion', 'sku'),)


class Region(models.Model):
    idregion = models.AutoField(db_column='idRegion', primary_key=True)  # Field name made lowercase.
    region = models.CharField(max_length=45)
    director = models.CharField(db_column='Director', max_length=45, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'region'


class ResumenRuta(models.Model):
    iddeposito = models.IntegerField()
    idruta = models.IntegerField(db_column='idRuta')  # Field name made lowercase.
    tiporuta = models.IntegerField(db_column='tipoRuta', blank=True, null=True)  # Field name made lowercase.
    tipomercado = models.IntegerField(db_column='tipoMercado', blank=True, null=True)  # Field name made lowercase.
    clientesprog = models.IntegerField(db_column='clientesProg', blank=True, null=True)  # Field name made lowercase.
    clientesvp = models.IntegerField(db_column='clientesVP', blank=True, null=True)  # Field name made lowercase.
    clientesc = models.IntegerField(db_column='clientesC', blank=True, null=True)  # Field name made lowercase.
    clientescv = models.IntegerField(db_column='clientesCV', blank=True, null=True)  # Field name made lowercase.
    clientesvnp = models.IntegerField(db_column='clientesVNP', blank=True, null=True)  # Field name made lowercase.
    clientesm2c = models.IntegerField(db_column='clientesM2C', blank=True, null=True)  # Field name made lowercase.
    cajaspfp = models.DecimalField(db_column='cajasPFP', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    cajasef = models.DecimalField(db_column='cajasEF', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    cajaspsiop = models.DecimalField(db_column='cajasPSIOP', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    cajasesio = models.DecimalField(db_column='cajasESIO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    firmaelectroncia = models.TimeField(db_column='firmaElectroncia', blank=True, null=True)  # Field name made lowercase.
    salidacedis = models.TimeField(db_column='salidaCedis', blank=True, null=True)  # Field name made lowercase.
    traslado1cliente = models.TimeField(db_column='traslado1Cliente', blank=True, null=True)  # Field name made lowercase.
    tiemposervicio = models.TimeField(db_column='tiempoServicio', blank=True, null=True)  # Field name made lowercase.
    tiempotraslado = models.TimeField(db_column='tiempoTraslado', blank=True, null=True)  # Field name made lowercase.
    trasladoultimocliente = models.TimeField(db_column='trasladoUltimoCliente', blank=True, null=True)  # Field name made lowercase.
    llegadacedis = models.TimeField(db_column='llegadaCedis', blank=True, null=True)  # Field name made lowercase.
    tiempocedis = models.TimeField(db_column='tiempoCedis', blank=True, null=True)  # Field name made lowercase.
    fechaoperacion = models.DateField(db_column='fechaOperacion')  # Field name made lowercase.
    odometroini = models.IntegerField(blank=True, null=True)
    odometrofin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resumen_ruta'
        unique_together = (('iddeposito', 'idruta', 'fechaoperacion'),)


class Ruta(models.Model):
    iddeposito = models.IntegerField(db_column='idDeposito')  # Field name made lowercase.
    idruta = models.IntegerField(db_column='idRuta')  # Field name made lowercase.
    clavetiporuta = models.IntegerField(blank=True, null=True)
    tiporuta = models.CharField(max_length=45, blank=True, null=True)
    clasificacionruta = models.CharField(max_length=45, blank=True, null=True)
    categoriaruta = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    grupo = models.IntegerField(blank=True, null=True)
    vehiculo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ruta'
        unique_together = (('iddeposito', 'idruta'),)


class Rutascambios(models.Model):
    idrutascambios = models.AutoField(db_column='idrutasCambios', primary_key=True)  # Field name made lowercase.
    idoperacion = models.ForeignKey(Operaciones, models.DO_NOTHING, db_column='idoperacion')
    idgruposupervision = models.ForeignKey(Gruposupervision, models.DO_NOTHING, db_column='idgruposupervision')
    ruta = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)
    tmercado = models.IntegerField(db_column='tMercado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rutascambios'


class Sabor(models.Model):
    idsabor = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'sabor'


class Segmento(models.Model):
    idsegmento = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'segmento'


class Seguimiento(models.Model):
    idseguimiento = models.IntegerField(primary_key=True)
    iddeposito = models.ForeignKey(Deposito, models.DO_NOTHING, db_column='idDeposito')  # Field name made lowercase.
    idnotificador = models.ForeignKey(Notificador, models.DO_NOTHING, db_column='idnotificador')
    estatus = models.IntegerField()
    observaciones = models.TextField(blank=True, null=True)
    fechanotificacion = models.DateTimeField(db_column='fechaNotificacion')  # Field name made lowercase.
    ip = models.CharField(max_length=45, blank=True, null=True)
    puerto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seguimiento'


class Tiempos(models.Model):
    celda = models.IntegerField()
    idoperacion = models.ForeignKey(Operaciones, models.DO_NOTHING, db_column='idoperacion')
    fecha = models.DateField()
    r_informacion = models.TimeField()
    c_espera = models.TimeField()
    f_disenio = models.TimeField()
    t_disenio = models.TimeField()
    t_msio = models.TimeField()

    class Meta:
        managed = False
        db_table = 'tiempos'
        unique_together = (('celda', 'idoperacion', 'fecha'),)


class Unidades(models.Model):
    idunidades = models.AutoField(db_column='idUnidades', primary_key=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    capacidad = models.IntegerField()
    palets = models.IntegerField()
    tipodepalet = models.IntegerField(db_column='TipoDePalet', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unidades'


class Usrcambios(models.Model):
    idoperacion = models.ForeignKey(Operaciones, models.DO_NOTHING, db_column='idoperacion')
    numempleado = models.IntegerField(db_column='NumEmpleado')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    psw = models.CharField(db_column='Psw', max_length=45)  # Field name made lowercase.
    ppp = models.IntegerField(db_column='PPP', blank=True, null=True)  # Field name made lowercase.
    nivel = models.IntegerField(blank=True, null=True)
    asignado = models.IntegerField(blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usrcambios'
        unique_together = (('numempleado', 'idoperacion'),)


class Usuarios(models.Model):
    idusuarios = models.AutoField(db_column='idUsuarios', primary_key=True)  # Field name made lowercase.
    idnivel = models.IntegerField(db_column='idNivel')  # Field name made lowercase.
    usuario = models.CharField(max_length=45)
    clave = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    puesto = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)
    puerto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'


class Vgen(models.Model):
    idvgen = models.IntegerField(db_column='idVgen', primary_key=True)  # Field name made lowercase.
    version = models.FloatField(db_column='Version')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vgen'


class Zona(models.Model):
    idzona = models.AutoField(db_column='idZona', primary_key=True)  # Field name made lowercase.
    idregion = models.ForeignKey(Region, models.DO_NOTHING, db_column='idRegion')  # Field name made lowercase.
    zona = models.CharField(max_length=45)
    gerentezona = models.CharField(db_column='gerenteZona', max_length=45)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zona'
