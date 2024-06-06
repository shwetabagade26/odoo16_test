from odoo import fields , models, api 

class Event(models.Model):
    _name='event.event'
    _description = "This handles the event management of the Company"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    start_date = fields.Date(string = "Start Date")
    end_date = fields.Date(string = "End Date")
    organiser_id = fields.Many2one('event.organiser' , string="Organiser")
    attendee_ids = fields.Many2many('event.attendee' , string= "Attendee IDs")
    duration = fields.Float(string="Duration", compute= '_compute_days')


    attendees_count = fields.Integer(compute='_compute_attendees_count', string="Attendees Count")

    @api.depends('start_date','end_date')
    def _compute_days(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                difference = (rec.end_date - rec.start_date).days
                rec.duration = difference
            else:
             rec.duration = 0  

    

    def _compute_attendees_count(self):
        for rec in self:
            rec.attendees_count = self.env['event.attendee'].search_count([('name', '=', rec.id)])

    def action_view_attendees(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Attendees Registered',
            'view_mode': 'tree,form',
            'res_model': 'event.attendee',
            'domain': [('name', '=', self.id)],
            'context': dict(self._context),
        }