# -*- coding: utf-8 -*-


from odoo import models, fields, api

class BibliotecaSocio(models.Model):
    _name = 'biblioteca.socio'
    _description = 'Socio de la biblioteca'

    # Atributos
    nombre = fields.Char('Nombre', required=True)
    apellido = fields.Char('Apellido', required=True)
    identificador = fields.Char('Identificador', required=True, index=True, unique=True)

    # Relación uno a muchos con los cómics prestados
    comics_prestados = fields.One2many('biblioteca.prestamo', 'socio_id', string='Cómics Prestados')


# Agrega el modelo BibliotecaSocio a la herencia de 'base.archive' si quieres usar la funcionalidad de activo
# _inherit = ['base.archive']