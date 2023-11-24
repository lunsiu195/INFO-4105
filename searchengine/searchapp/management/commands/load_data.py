# searchapp/management/commands/load_data.py

from django.core.management.base import BaseCommand
from searchapp.models import CrawledPage
import json
import os 

class Command(BaseCommand):
    help = 'Load data from output.json file into the database'

    def handle(self, *args, **options):
         # Get the path to the 'output.json' file
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../scrapy_engine/output.json')
      
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
      
                for item in data:
                    print(f"Processing item: {item}")
                    CrawledPage.objects.create(
                        url=item['url'],
                        title=item['title'],

                    )
                    print("Item processed and saved.")
        else:
          self.stdout.write(self.style.ERROR('File not found: {}'.format(file_path)))  
