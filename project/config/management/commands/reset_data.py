import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from . import fixtures


class Command(BaseCommand):
    """
    Command for Restoring fixtures
    """
    help = "Reset database and load fixtures to Database."

    def handle(self, *args, **options):
        print "Re-initializing Virtual Environment...\nPlease Wait..."
        print "Deleting Data from Database...\nPlease Wait..."
        call_command("reset_db", interactive=False, router="default")
        print "Re-creating database schema...\nPlease Wait..."
        call_command("syncdb", interactive=False)
        print "Loading schema from json fixtures to database...\nPlease Wait..."
        try:
            self.load_data()
            print "Restore is now complete!"
        except Warning:
            print "Error(s) found in restoring data"
        call_command("validate", interactive=False)

    def load_data(self):
         # Order matters here due to FK constrains!
        for x in fixtures:
            fixture_json_name = str(x) + ".json"
            call_command("loaddata", fixture_json_name)