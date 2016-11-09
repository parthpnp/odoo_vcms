# -*- coding: utf-8 -*-

from openerp import models, fields, api

class vcms_demo(models.Model):
    _name = 'vcms_demo.vcms_demo'

    name = fields.Char(string="Company Name")
    address = fields.Text(string="Address")
    number = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    description = fields.Text()
    img = fields.Binary("Image")
    city = fields.Many2one('city_demo.city_demo',string="City")


class city_demo(models.Model):
	_name = 'city_demo.city_demo'

	name = fields.Char(string="City Name")
