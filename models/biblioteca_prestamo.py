# -*- coding: utf-8 -*-

from odoo import models, fields

class BibliotecaPrestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Préstamo de cómic'

    # Atributos
    comic_id = fields.Many2one('biblioteca.comic', string='Cómic', required=True)
    socio_id = fields.Many2one('biblioteca.socio', string='Socio', required=True)
    fecha_prestamo = fields.Date('Fecha de préstamo', default=fields.Date.today())
    fecha_devolucion = fields.Date('Fecha de devolución')