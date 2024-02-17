# -*- coding: utf-8 -*-


from odoo import models, fields, api

class BibliotecaSocio(models.Model):
    _name = 'biblioteca.socio'
    _description = 'Socio de la biblioteca'
    _rec_name = 'nombreCompleto'
    
    nombre = fields.Char('Nombre')
    apellido = fields.Char('Apellido')
    identificador = fields.Char('Identificador')

    #idSocio = fields.Many2many('biblioteca.prestamo', 'idSocio', string='Préstamos')

    nombreCompleto = fields.Char('Nombre Completo', compute='_compute_nombre_completo', store=True)

    @api.depends('nombre', 'apellido')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombreCompleto = f"{record.nombre} {record.apellido}"