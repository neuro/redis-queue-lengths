# redis-queue-lengths
Simple Docker image to post the length of Redis queues in 10s intervals to an InfluxDB instance. Automated builds of this image are available on the Docker Hub as [neurology/redis-queue-lengths](https://hub.docker.com/r/neurology/redis-queue-lengths/).

## Configuration
The script reads four environment variables, _REDIS\_URL_, _INFLUXDB\_HOST_, _INFLUXDB\_PORT_, _INFLUXDB\_DATABASE_, and _QUEUES_. _QUEUES_ can be a comma-separated list of Redis queue names.

## Example
```
docker run \
  -e REDIS_URL="redis://localhost" \
  -e INFLUXDB_HOST="localhost" \
  -e INFLUXDB_PORT="8086" \
  -e INFLUXDB_DATABASE="queue-lengths" \
  -e QUEUES="jobs, ids, telephone_numbers" \
  neurology/redis-queue-lengths
```
