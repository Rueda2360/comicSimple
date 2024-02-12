# -*- coding: utf-8 -*-
from odoo import models, fields

class Prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Préstamo de cómics'

    comic_id = fields.Many2one('biblioteca.comic', string='Cómic', required=True)
    fecha_inicio = fields.Date('Fecha de inicio', default=fields.Date.today(), required=True)
    fecha_fin = fields.Date('Fecha de finalización', required=True)
    prestado_a = fields.Many2one('res.partner', string='Prestado a', required=True)
    devuelto = fields.Boolean('Devuelto', default=False)

    #if devuelto
    def marcar_devuelto(self):
        self.devuelto = True
