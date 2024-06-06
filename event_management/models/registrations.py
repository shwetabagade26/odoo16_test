from odoo import fields , models, api 

class Registrations(models.Model):
    _name='event.registrations'
    _description = "This handles the Registration of the Event"

    attendee_id = fields.Many2one('event.attendee' , string="Attendee ID")
    event_id = fields.Many2one('event.event' , string="Event ID")
    registration_date = fields.Date(string = "Registration Date")
    state = fields.Selection([('draft','Draft'),('confirm','Confirm'),
                                 ('cancelled','Cancelled')], default ='draft', string="State")
    
    def action_confirm(self):
        self.state = 'confirm'
        
        template_id = self.env.ref('event_management.event_registration_email_template').id
        for rec in self:
            if rec.attendee_id.email:
                email_values = {
                    'email_to': rec.attendee_id.email,
                    'auto_delete': False,
                }
                self.env['mail.template'].browse(template_id).send_mail(rec.id, email_values=email_values, force_send=True)
        

    
    def action_cancel(self):
        self.state = 'cancelled'