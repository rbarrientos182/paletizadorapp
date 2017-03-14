# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


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


class Zona(models.Model):
    idzona = models.AutoField(db_column='idZona', primary_key=True)  # Field name made lowercase.
    idregion = models.ForeignKey('Region', models.DO_NOTHING, db_column='idRegion')  # Field name made lowercase.
    zona = models.CharField(max_length=45)
    gerentezona = models.CharField(db_column='gerenteZona', max_length=45)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zona'


class Region(models.Model):
    idregion = models.AutoField(db_column='idRegion', primary_key=True)  # Field name made lowercase.
    region = models.CharField(max_length=45)
    director = models.CharField(db_column='Director', max_length=45, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'region'
