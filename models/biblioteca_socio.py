# -*- coding: utf-8 -*-


from odoo import models, fields, api

class BibliotecaSocio(models.Model):
    _name = 'biblioteca.socio'
    _description = 'Socio de la biblioteca'

    nombre = fields.Char('Nombre')
    apellido = fields.Char('Apellido')
    identificador = fields.Char('Identificador')

    idSocio = fields.One2many('biblioteca.prestamo', 'idSocio', string='Préstamos')
