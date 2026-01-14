from django.core.management.base import BaseCommand
from django.db import connection, connections

class Command(BaseCommand):
    help = "Find all /raw/upload/ URLs in the database"

    def handle(self, *args, **options):
        self.stdout.write("\n" + "="*60)
        self.stdout.write("🔍 Searching for /raw/upload/ URLs in database...\n")
        
        db_engine = connections['default'].settings_dict['ENGINE']
        is_postgres = 'postgresql' in db_engine
        
        with connection.cursor() as cursor:
            if is_postgres:
                # PostgreSQL
                cursor.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public'
                    AND table_type = 'BASE TABLE'
                """)
            else:
                # MySQL
                cursor.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = DATABASE()
                    AND table_type = 'BASE TABLE'
                """)
            
            tables = cursor.fetchall()
            found_count = 0
            
            for (table_name,) in tables:
                # Get all text columns
                if is_postgres:
                    cursor.execute(f"""
                        SELECT column_name, data_type
                        FROM information_schema.columns
                        WHERE table_schema = 'public'
                        AND table_name = '{table_name}'
                        AND (data_type LIKE '%text%' OR data_type LIKE '%varchar%' OR data_type = 'json')
                    """)
                else:
                    cursor.execute(f"""
                        SELECT column_name, column_type
                        FROM information_schema.columns
                        WHERE table_schema = DATABASE()
                        AND table_name = '{table_name}'
                        AND (column_type LIKE '%text%' OR column_type LIKE '%varchar%' OR column_type = 'json')
                    """)
                
                columns = cursor.fetchall()
                
                for column_name, column_type in columns:
                    try:
                        # Search for /raw/upload/ in this column
                        cursor.execute(f"""
                            SELECT COUNT(*) FROM "{table_name}"
                            WHERE "{column_name}" LIKE '%/raw/upload/%'
                        """)
                        
                        count = cursor.fetchone()[0]
                        if count > 0:
                            found_count += count
                            self.stdout.write(
                                self.style.WARNING(
                                    f"⚠️  {table_name}.{column_name}: {count} records with /raw/upload/"
                                )
                            )
                    except Exception as e:
                        pass
        
        self.stdout.write("\n" + "="*60)
        self.stdout.write(self.style.SUCCESS(
            f"✓ Search complete! Total found: {found_count} occurrences"
        ))
        self.stdout.write("="*60 + "\n")
