import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from ...models import Restaurant

class Command(BaseCommand):
    help = 'Import data from CSV file into the database'

    def handle(self, *args, **kwargs):
        csv_file = 'C:/Users/SIDDESH VICHARE/Downloads/Restuarant Search/restaurantapp/restuarantsearch/management/commands/restaurants_small.csv'

        try:
            df = pd.read_csv(csv_file)

            for _, row in df.iterrows():
                # Print row data to debug
                print(row)

                # Create or get the Restaurant object
                restaurant, created = Restaurant.objects.get_or_create(
                    name=row['name'],
                    defaults={
                        'location': row['location'],
                        'Item':row['items'],
                        'lat_long': row['lat_long'],
                        'full_details': row['full_details'],  # Assuming full_details is a JSON string in CSV
                    }
                )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to import data: {str(e)}"))
