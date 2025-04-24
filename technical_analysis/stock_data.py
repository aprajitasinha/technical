from datetime import datetime
import requests
import psycopg2
import ipdb
DB_CONFIG = {
    "dbname": "candleanalytics",
    "user": "aryanpatel",
    "password": "12345",
    "host": "localhost",
    "port": "5432",
}

STOCKS = [
    "ADANIENT", "ADANIGREEN","UPL"
]

INTERVALS = {
    "1m": 1,
    "2m": 2,
    "3m": 3,
    "5m": 5,
    "10m": 10,
    "15m": 15,
    "30m": 30,
    "1h": 60,
    "4h": 240,
    "1d": 1440,
    "1w": 10080,
    "1mo": 43200,
}

BASE_URL = "https://groww.in/v1/api/charting_service/v4/chart/exchange/NSE/segment/CASH/{stock}?endTimeInMillis={end}&intervalInMinutes={interval}&startTimeInMillis={start}"

def get_ms_timestamp(dt):
    return int(dt.timestamp() * 1000)

def ensure_table_exists(cursor, stock, interval_name):
    cursor.execute(f'CREATE SCHEMA IF NOT EXISTS "{stock}";')
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS "{stock}"."candle_{interval_name}" (
            timestamp TIMESTAMP PRIMARY KEY,
            open NUMERIC,
            high NUMERIC,
            low NUMERIC,
            close NUMERIC,
            volume NUMERIC
        );
    ''')
    
def fetch_and_store_data():
    today = datetime.now().replace(hour=9, minute=15, second=0, microsecond=0)
    start_time = today
    end_time = today.replace(hour=15, minute=30)

    start_ms = get_ms_timestamp(start_time)
    end_ms = get_ms_timestamp(end_time)

    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    for stock in STOCKS:
        for interval_name, interval_val in INTERVALS.items():
            try:
                ensure_table_exists(cursor, stock, interval_name)
                conn.commit()  # Commit table creation

                url = BASE_URL.format(stock=stock, start=start_ms, end=end_ms, interval=interval_val)
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                print(f"URL: {url}")
                print(f"Status Code: {response.status_code}")
                print(f"Response: {response.json()}")


                candles = data.get("candles", [])
                if not candles:
                    print(f"No data for {stock} - {interval_name}")
                    continue
                # ipdb.set_trace()
                insert_query = f'''
                    INSERT INTO "{stock}"."candle_{interval_name}" (timestamp, open, high, low, close, volume)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (timestamp) DO NOTHING
                '''

                # for candle in candles:
                #     try:
                #         ts = candle[0] // 1000
                #         dt = datetime.fromtimestamp(ts)
                #         values = (dt, *candle[1:6])
                #         cursor.execute(insert_query, values)
                # ipdb.set_trace()
                for candle in candles:
                    print("Raw candle:", candle)
                    try:
                        ts = candle[0]
                        print("Raw ts (ms):", candle[0], " | Converted to seconds:", ts)
                        dt = datetime.fromtimestamp(ts)
                        print("Datetime:", dt)
                        values = (dt, *candle[1:6])
                        print(f"Inserting values: {values}")
                        cursor.execute(insert_query, values)
                    except Exception as e:
                        print(f"Insert error for {stock} - {interval_name} at {dt}: {e}")
                        conn.rollback()  # Reset bad transaction
                        continue

                conn.commit()
                print(f"Inserted {len(candles)} rows into {stock}.candle_{interval_name}")

            except Exception as e:
                print(f"Error for {stock} - {interval_name} chunk: {e}")
                conn.rollback()  # Reset transaction
                continue

    cursor.close()
    conn.close()
    
if __name__ == "__main__":
    fetch_and_store_data()
    
    