from django.contrib.sites.models import Site
from django.test import override_settings

from openzaak.utils.tests import APICMISTestCase

from ..models import EnkelvoudigInformatieObject
from .factories import EnkelvoudigInformatieObjectFactory


@override_settings(CMIS_ENABLED=True)
class QueryTests(APICMISTestCase):
    """
    Test that the query interface works with CMIS as backend.
    """

    @classmethod
    def setUpTestData(cls):
        site = Site.objects.get_current()
        site.domain = "testserver"
        site.save()

    def test_filter(self):
        EnkelvoudigInformatieObjectFactory.create(identificatie="001")
        eio2 = EnkelvoudigInformatieObjectFactory.create(identificatie="002")

        eios = EnkelvoudigInformatieObject.objects.filter(identificatie="002")

        self.assertEqual(
            [eio.identificatie for eio in eios], [eio2.identificatie],
        )

    def test_filter_then_all(self):
        EnkelvoudigInformatieObjectFactory.create(identificatie="001")
        eio2 = EnkelvoudigInformatieObjectFactory.create(identificatie="002")

        eios = EnkelvoudigInformatieObject.objects.filter(identificatie="002").all()

        self.assertEqual(
            [eio.identificatie for eio in eios], [eio2.identificatie],
        )

    def test_chained_filter(self):
        EnkelvoudigInformatieObjectFactory.create(identificatie="001")
        EnkelvoudigInformatieObjectFactory.create(identificatie="002")

        eios = EnkelvoudigInformatieObject.objects.filter(identificatie="001").filter(
            identificatie="002"
        )

        self.assertEqual(list(eios), [])

    def test_all(self):
        eio1 = EnkelvoudigInformatieObjectFactory.create(identificatie="001")
        eio2 = EnkelvoudigInformatieObjectFactory.create(identificatie="002")

        eios = EnkelvoudigInformatieObject.objects.all()

        self.assertEqual(
            {eio.identificatie for eio in eios},
            {eio1.identificatie, eio2.identificatie},
        )
