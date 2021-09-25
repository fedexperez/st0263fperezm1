from environs import Env
import psycopg2

env = Env()
env.read_env()

psycopg2.connect(
            host=env('POSTGRES_HOST'), 
            database=env('POSTGRES_DB'), 
            user=env('POSTGRES_USER'), 
            password=env('POSTGRES_PASSWORD')
        )