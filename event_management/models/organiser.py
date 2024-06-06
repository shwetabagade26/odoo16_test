from odoo import fields , models, api 

class Organiser(models.Model):
    _name='event.organiser'
    _description = "This handles the Organiser of the Event"

    name= fields.Char(string ="Name")
    email= fields.Char(string="Email")
    phone= fields.Char(string ="Phone")
    # user_id
    event_ids = fields.One2many('event.event','organiser_id',string="Event IDs")
