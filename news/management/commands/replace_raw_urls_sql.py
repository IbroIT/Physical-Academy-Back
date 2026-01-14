from django.core.management.base import BaseCommand
from django.db import connection, transaction

class Command(BaseCommand):
    help = "Replace /raw/upload/ → /image/upload/ using direct SQL for maximum performance"

    def handle(self, *args, **options):
        self.stdout.write("\n" + "="*60)
        self.stdout.write("🚀 Starting direct SQL replacement...\n")
        
        total_affected = 0
        
        with connection.cursor() as cursor:
            # Get all tables and columns
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = DATABASE()
                AND table_type = 'BASE TABLE'
            """)
            
            tables = cursor.fetchall()
            
            for (table_name,) in tables:
                # Get all text columns
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
                        # Check if column contains /raw/upload/
                        cursor.execute(f"""
                            SELECT COUNT(*) FROM `{table_name}`
                            WHERE `{column_name}` LIKE '%/raw/upload/%'
                        """)
                        
                        count = cursor.fetchone()[0]
                        
                        if count > 0:
                            # Perform the replacement
                            with transaction.atomic():
                                cursor.execute(f"""
                                    UPDATE `{table_name}`
                                    SET `{column_name}` = REPLACE(`{column_name}`, '/raw/upload/', '/image/upload/')
                                    WHERE `{column_name}` LIKE '%/raw/upload/%'
                                """)
                                
                                affected = cursor.rowcount
                                total_affected += affected
                                
                                self.stdout.write(
                                    self.style.SUCCESS(
                                        f"✔ {table_name}.{column_name}: {affected} records updated"
                                    )
                                )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(f"✗ Error in {table_name}.{column_name}: {str(e)}")
                        )
        
        self.stdout.write("\n" + "="*60)
        self.stdout.write(self.style.SUCCESS(
            f"✓ Complete! Total records updated: {total_affected}"
        ))
        self.stdout.write("="*60 + "\n")
