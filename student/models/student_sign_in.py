from odoo import fields, models, api


class StudentSignIn(models.Model):
    _name = 'student.sign_in'

    # STUDENT DATA
    name = fields.Char('Name')

    birthday = fields.Date('Birthday')

    nationality = fields.Char('Nationality')

    place_of_birth = fields.Char('Naturalness')

    identification_number = fields.Char('Identification number')

    genre = fields.Char('Genre')

    # ADDRESS
    street = fields.Char('Street')

    street2 = fields.Char('Street 2')

    city = fields.Char('City')

    state = fields.Char('State')

    country = fields.Many2one('res.country', 'Country')

    zip_code = fields.Char('Zip Code')

    # RESPONSIBLE FOR STUDENT
    responsible_name = fields.Char('Responsible name')

    responsible_phone = fields.Char('Responsible phone')

    responsible_email = fields.Char('Responsible e-mail')

    responsible_profession = fields.Char('Responsible profession')

    # RESPONSIBLE FOR STUDENT
    responsible2_name = fields.Char('2nd Responsible name')

    responsible2_phone = fields.Char('2nd Responsible phone')

    responsible2_email = fields.Char('2nd Responsible email')

    responsible2_profession = fields.Char('2nd Responsible profession')

    # MORE INFORMATION
    emergency_number = fields.Char('Emergency number')

    emergency_number2 = fields.Char('Emergency number')

