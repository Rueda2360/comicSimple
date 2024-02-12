# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BibliotecaPrestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Préstamo de cómic'

    idComic = fields.Many2one('biblioteca.comic', string='Cómic')
    idSocio = fields.Many2one('biblioteca.socio', string='Socio', required=True)
    fechaInicio = fields.Date('Fecha de inicio', default=fields.Date.today(), required=True)
    fechaDevolucion = fields.Date('Fecha de devolución prevista', required=True)

    devuelto = fields.Boolean('Devuelto', default=False)

    def devolver_comic(self):
        self.devuelto = True
