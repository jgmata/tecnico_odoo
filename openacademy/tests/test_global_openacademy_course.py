# -*- encoding: utf-8 -*-

from odoo.tests.common import TransactionCase


class GlobalTestOpenAcademyCourse(TransactionCase):

    def setUp(self):

        super(GlobalTestOpenAcademyCourse, self).setUp()
        self.variable = 'Helo World'
        self.course = self.env['openacademy.course']

    def create_course(self, course_name, course_description, course_responsible_id):
        course_id = self.course.create({
            'name': course_name,
            'description': course_description,
            'responsible_id': course_responsible_id
        })
        return course_id

    def test_01_same_name_description(self):
        self.create_course('JOSE', 'JOSE', None)




