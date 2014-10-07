# -*- coding: UTF-8 -*-

import tempfile

from odoorpc.tests import LoginTestCase
from odoorpc import error


class TestReport(LoginTestCase):

    def test_report_download_pdf(self):
        model = 'res.company'
        report_name = 'preview.report'
        ids = self.odoo.get(model).search([])[:20]
        report = self.odoo.report.download(report_name, ids)
        with tempfile.TemporaryFile(mode='wb', suffix='.pdf') as file_:
            file_.write(report.read())

    def test_report_download_qweb_pdf(self):
        model = 'account.invoice'
        report_name = 'account.report_invoice'
        ids = self.odoo.get(model).search([])[:10]
        report = self.odoo.report.download(report_name, ids)
        with tempfile.TemporaryFile(mode='wb', suffix='.pdf') as file_:
            file_.write(report.read())

    def test_report_download_sxw(self):
        model = 'ir.model'
        report_name = 'ir.model.overview'
        ids = self.odoo.get(model).search([])[:20]
        report = self.odoo.report.download(report_name, ids)
        with tempfile.TemporaryFile(mode='wb', suffix='.sxw') as file_:
            file_.write(report.read())

    def test_report_download_wrong_report_name(self):
        self.assertRaises(
            error.RPCError,
            self.odoo.report.download, 'wrong_report', [1])

    def test_report_list(self):
        res = self.odoo.report.list()
        self.assertIsInstance(res, dict)
        self.assertIn('res.company', res)
        self.assertIn('preview.report', res['res.company'][0]['report_name'])

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: