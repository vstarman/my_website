from django.core.management.base import BaseCommand, CommandError
from apps.about.models import Poll


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # 必须实现的方法
    def handle(self, *args, **options):
        for poll_id in options['poll_id']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write('Successfully closed poll "%s"' % poll_id)