from django.core.management.base import BaseCommand, CommandError
from partners.models import Partner


class Command(BaseCommand):
    help = 'Create fake partner'

    def add_arguments(self, parser):
        parser.add_argument('id', nargs='+', type=int)

    def handle(self, *args, **options):
        for partner_id in options['id']:
            try:
                partner = Partner.objects.get(pk=partner_id)
            except Partner.DoesNotExist:
                raise CommandError('Partner "%s" does not exist' % partner_id)

            partner.name = 'Modify'
            partner.save()

            self.stdout.write(self.style.SUCCESS(
                'Successfully changed partner "%s"' % partner.name)
            )
