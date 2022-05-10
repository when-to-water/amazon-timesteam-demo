import boto3
import time

DB_NAME = "demo"
TBL_NAME = "IoT"
CURRENT_TIME = str(int(time.time() * 1000))

write_client = boto3.client("timestream-write")

dimension = [
    {"Name": "fleet", "Value": "test"},
    {"Name": "fuel_capacity", "Value": "test"},
    {"Name": "load_capacity", "Value": "test"},
    {"Name": "make", "Value": "test"},
    {"Name": "model", "Value": "test"},
    {"Name": "truck_id", "Value": "test"},
]
record = {
    "Time": CURRENT_TIME,
    "Dimensions": dimension,
    "MeasureName": "test",
    "MeasureValue": "11.1",
    "MeasureValueType": "DOUBLE",
}
record = [record]

try:
    response = write_client.write_records(
        DatabaseName=DB_NAME, TableName=TBL_NAME, Records=record
    )
    print(response)
except Exception as e:
    print(f"An exeption occured: {e}")
