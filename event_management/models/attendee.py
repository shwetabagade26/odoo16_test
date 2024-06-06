from odoo import fields , models, api 

class Attendee(models.Model):
    _name='event.attendee'
    _description = "This handles the Attendance of the Event"

    name= fields.Char(string ="Name")
    email= fields.Char(string="Email")
    phone= fields.Char(string ="Phone")
    # user_id
    event_ids = fields.Many2many('event.event' ,string="Event IDs")

    # @api.onchange('')
    def _on_change_phone(self):
        for rec in self:
            user_id = self.env['res.users'].create({
                'partner_id': rec.name,
                'email': rec.email,
                'phone': rec.phone,
            })
        return user_id

    