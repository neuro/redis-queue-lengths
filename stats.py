import os
from time import sleep
from redis import StrictRedis
from influxdb import InfluxDBClient

redis_url = os.environ['REDIS_URL']
influxdb_host = os.environ['INFLUXDB_HOST']
influxdb_port = os.environ['INFLUXDB_PORT']
influxdb_database = os.environ.get('INFLUXDB_DATABASE', 'queue-lengths')
queues = os.environ.get('QUEUES', 'dataset-jobs, metadata-jobs')

r = StrictRedis.from_url(redis_url)
i = InfluxDBClient(influxdb_host, influxdb_port, "", "", influxdb_database)
i.create_database(influxdb_database)

queues = ''.join(queues.split())
queues = queues.split(',')

while True:
    measurements = []
    for queue in queues:
        length = r.llen(queue)
        measurement = {
            "measurement": "queue_length",
            "fields": {
                "value": length
            },
            "tags": {
                "queue": queue
            }
        }
        measurements.append(measurement)
    i.write_points(measurements)
    sleep(10)
