from cleaner import clean_data
from transform import transform_to_star_schema

def main():
    clean_data()
    transform_to_star_schema()
    print("ETL Pipeline completed!")

if __name__ == "__main__":
    main()
    #