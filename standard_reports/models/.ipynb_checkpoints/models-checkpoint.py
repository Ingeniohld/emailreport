# -*- coding: utf-8 -*-

from odoo import models, fields, api
import xlrd
import tempfile
import binascii
from odoo.exceptions import RedirectWarning, UserError, ValidationError

class standard_reports(models.Model):
    _name = 'standard.reports'
    _description = 'standard_reports'

    name = fields.Char(compute='_get_data')
    value = fields.Integer()
    
    @api.depends('value')
    def _get_data(self):
        for rec in self :
            document = self.env['documents.document'].search([
                ('id', '=', 95)])
            attach = self.env['ir.attachment'].search([('id','=',document.attachment_id.id)])
            fp = tempfile.NamedTemporaryFile(suffix=".xlsx")
            fp.write(binascii.a2b_base64(attach.datas))
            fp.seek(0)
            workbook = xlrd.open_workbook(fp.name)
            sheet = workbook.sheet_by_index(0)
            for row_no in range(sheet.nrows):
                if row_no <= 0:
                    fields = map(lambda row:row.value.encode('utf-8'), sheet.row(row_no))
                else:
                    line = list(map(lambda row:isinstance(row.value, str) and row.value.encode('utf-8') or str(row.value), sheet.row(row_no)))
                    rec.name = line[0]
#                     exit
#                     raise UserError(line[1])
