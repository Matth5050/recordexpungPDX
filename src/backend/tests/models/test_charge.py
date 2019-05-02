import unittest

from tests.factories.charge_factory import ChargeFactory
from tests.factories.case_factory import CaseFactory


class TestCaseWithDisposition(unittest.TestCase):

    def setUp(self):
        self.charge = ChargeFactory.build()

    def test_it_initializes_simple_statute(self):
        self.charge['statute'] = '1231235B'
        charge = ChargeFactory.save(self.charge)

        assert charge.statute == '1231235B'

    def test_it_normalizes_statute(self):
        self.charge['statute'] = '-123.123(5)()B'
        charge = ChargeFactory.save(self.charge)

        assert charge.statute == '1231235B'

    def test_it_converts_statute_to_uppercase(self):
        self.charge['statute'] = '-123.123(5)()b'
        charge = ChargeFactory.save(self.charge)

        assert charge.statute == '1231235B'

    def test_it_retrieves_its_parent_instance(self):
        case = CaseFactory.create()
        charge = ChargeFactory.create(case=case)

        assert charge.case()() is case
