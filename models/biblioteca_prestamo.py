# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
from openerp.exceptions import ValidationError

class BibliotecaPrestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Préstamo de cómic'

    idComic = fields.Many2one('biblioteca.comic', string='Cómic')
    idSocio = fields.Many2one('biblioteca.socio', string='Socio', required=True)
    fechaInicio = fields.Date('Fecha de inicio', default=fields.Date.today(), required=True)
    fechaDevolucion = fields.Date('Fecha de devolución prevista', required=True)

#    nombreLibro = fields.Char(related='idComic.nombre', string='Nombre del Libro')
#    nombreSocio = fields.Char(related='idSocio.nombre', string='Nombre del Socio')
#    apellidosSocio = fields.Char(related='idSocio.apellido', string='Apellidos del Socio')
    
    devuelto = fields.Boolean('Devuelto', default=False)

    def devolver_comic(self):
        self.devuelto = True

    @api.constrains('fechaInicio')
    def funcionFechaPrestamo(self):
        for registro in self:
            if registro.fechaInicio and registro.fechaInicio > fields.Date.today():
                raise ValidationError('La fecha de préstamo no puede ser posterior al día de hoy.')

    @api.constrains('fechaDevolucion')
    def funcionFechaDevolucion(self):
        for registro in self:
            yesterday = fields.Date.today() - timedelta(days=1)
            if registro.fechaDevolucion and registro.fechaDevolucion < yesterday:
                raise ValidationError('La fecha prevista de vuelta no puede ser anterior al día de ayer.')
