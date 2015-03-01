import tarfile
import os
import re
import datetime
from django.core.management.base import BaseCommand
from django.core.management import call_command
from . import fixtures

class Command(BaseCommand):
    """
    Command for Backing up fixtures
    """
    help = "Backup Database to JSON objects."

    def handle(self, *args, **options):
        print "Starting the backing up process..."
        fixtures_dir = os.path.join(os.getcwd(), "fixtures")
        # used to delete old .json files
        pattern_json = "^.*.json"
        try:
            self.purge(fixtures_dir, pattern_json)
            print "\n Deleted old .json backup files..Please wait."
        except Exception:
             print "\n No .json file(s) found..Please wait.."
        # used to delete old backup files!
        pattern = "^(fixtures-\d+)[^\d].*.gz"
        try:
           # self.purge(fixtures_dir, pattern)
            print "\n Deleted .tar.gz backup file(s)..Please wait.."
        except Exception:
            print "\n No previous .tar.gz file(s) found..Please wait.."
        print "\n Dumping data from database to new json files..Please Wait..."
        try:
            self.dump_data(fixtures_dir)
            print " \n Json Fixtures created successfully. Compressing...Please Wait..."
            file_name = os.path.join(fixtures_dir, "fixtures") + "-" + datetime.datetime.now().strftime(
                "%d%m%Y%H%M%S") + ".tar.gz"
            #file_name = "db/bak.tar.gz"
            tar = tarfile.open(file_name, "w:gz")
            tar.add(fixtures_dir, arcname="fixtures")
            tar.close()
            print "\n Compressed tar file created at location: %s" % file_name
            print "\n Backup is now complete!"
        except Warning:
            print "Could not dump data! Please check folders/dependencies."

    def dump_data(self, fixtures_dir):
        for fixture in fixtures:
            fixture_json_name = str(fixture) + ".json"
            output_filename = os.path.join(fixtures_dir, fixture_json_name)
            output = open(output_filename, "w")
            call_command("dumpdata", fixture, format="json", indent=3, stdout=output)
            output.close()

    def purge(self, directory, pattern):
        try:
            for f in os.listdir(directory):
                if re.search(pattern, f):
                    os.remove(os.path.join(directory, f))
        except IOError:
            print "file(s) matching pattern not found"