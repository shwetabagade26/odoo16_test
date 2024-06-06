{
    "name": "Bista Event Management",
    "version": "1.0",
    "website": "https://www.bistasolutions.com/",
    "author": "Shweta",
    "description": """
        Odoo Test on 6th June 2024
    """,
    "category": "Sales",
    "depends": ['sale','base'],
    "data": [
        # security
        "security/ir.model.access.csv",
        "security/security.xml",
        # data
        "data/email_template_event.xml",
        # wizard
        "wizard/event_registration_details_wiz_view.xml",
        # views
        "views/event_view.xml",
        "views/attendee_view.xml",
        "views/organiser_view.xml",
        "views/registrations_view.xml",
        "views/menu.xml",
    ],
    "installable":True,
    "application":True,
    "license": "LGPL-3"
}