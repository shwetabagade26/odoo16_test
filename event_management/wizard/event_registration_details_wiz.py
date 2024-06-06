from odoo import api , models, fields
from io import BytesIO
import xlwt
import base64

class EventRegistrationDetailsWiz(models.TransientModel):
    _name = 'event.registration.details.wizard'
    _description = "This is a wizard to generate a report from start to end date of a particular event"

    date_from = fields.Date(string = "Date From")
    date_to = fields.Date(string = "Date To")

    def generate_excel(self):
        domain = []

        date_from = self.date_from

        if self.date_from:
            domain += [('start_date', '>=', date_from)]

        date_to=self.date_to

        if self.date_to:
            domain += [('end_date', '<=', date_to)]

        event_registrations_info = self.env["event.event"].search_read(domain)
        print("excel data--------",event_registrations_info)

        # Create the Excel workbook and worksheet
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Event Details Information')

        # Write the report title
        title_style = xlwt.easyxf('font: bold on; align: horiz center;')
        worksheet.write_merge(0, 0, 0, 5, 'Event Registration Report', title_style)
        worksheet.write_merge(1, 1, 0, 1, 'Date From:', xlwt.easyxf('font: bold on;'))
        worksheet.write_merge(1, 1, 2, 3, str(self.date_from))
        worksheet.write_merge(2, 2, 0, 1, 'Date To:', xlwt.easyxf('font: bold on;'))
        worksheet.write_merge(2, 2, 2, 2, str(self.date_to))
      
        # Write the headers for the account data
        header_style = xlwt.easyxf('font: bold on; align: horiz center;')
        worksheet.write(5, 0,  'Registration Date', header_style)       
        worksheet.write(5, 1, 'Organiser Name', header_style)
        worksheet.write(5, 2,  'Attendee Name', header_style)
        worksheet.write(5, 3,  'Event Name', header_style)
        worksheet.write(5, 4,  'Registration State', header_style)

        # Write the account data
        row = 6
        for data in event_registrations_info:
            worksheet.write(row, 0, str(data.get('name', '')))
            worksheet.write(row, 1, str(data.get('start_date', '')))
            worksheet.write(row, 2, str(data.get('end_date', '')))
            row += 1

        # Save the report file
        report_file = BytesIO()
        workbook.save(report_file)
        report_file.seek(0)

        filename = 'Event Registration Details.xls'
        attachment = self.env['ir.attachment'].create({
            'name': filename,
            'datas': base64.encodebytes(report_file.read()),
            'res_model': self._name,
            'res_id': self.id
        })

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'new',
        }