import os
import re
from django.core.management.base import BaseCommand, CommandError
from fastkml import kml
from apps.countries.models import Country


class Command(BaseCommand):
    args = 'Input kml file'
    help = 'Gets country kml data from file'

    def add_arguments(self, parser):
        parser.add_argument('kml-file', nargs="+", type=str, )


    def handle(self, *args, **options):
        PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
        kml_file = PROJECT_PATH + "/" + options['kml-file'][0]
        strip_code = re.compile(ur'ISO_A2=(.{2}).*')

        with open (kml_file, "r") as file:
            kml_string = file.read()

        k = kml.KML()
        k.from_string(kml_string)

        # placemarks = list(list(k.features())[0].features())
        # for placemark in placemarks:
        #     code = re.search(strip_code, placemark.description).group(1)
        #     qs = Country.objects.filter(code=code)
        #     if qs.count() == 1:
        #         country = qs.get()
        #         country.kml = placemark.to_string()
        #         country.save()

        placemarks = list(list(k.features())[0].features())
        for placemark in placemarks:
            code = placemark.extended_data.elements[2].value
            qs = Country.objects.filter(code=code)
            if qs.count() == 1:
                country = qs.get()
                try:
                    country.kml = placemark.to_string()
                    print "Saved kml for {0}".format(code)
                except Exception:
                    print "Could not save kml for {0}".format(code)
                country.save()
