# -*- coding: utf-8 -*-


from odoo import models, fields, api

class BibliotecaSocio(models.Model):
    _name = 'biblioteca.socio'
    _description = 'Socio de la biblioteca'

    nombre = fields.Char('Nombre', required=True)
    apellido = fields.Char('Apellido', required=True)
    identificador = fields.Char('Identificador', required=True, index=True, unique=True)

    comics_prestados = fields.One2many('biblioteca.prestamo', 'socio_id', string='Cómics Prestados')
