import sys
import datetime
import time
import random

from dsfaker.generators.autoincrement import AutoincrementWithGenerator
from dsfaker.generators.distributions import Normal
from dsfaker.generators.series import RepeatPattern

from storage import ImmutableStore, dt_to_nano_timestamp

if __name__ == "__main__":
    filesize = 2**27 # bytes
    write_at = 10000 # Hz

    pctg_numerics = 0.2

    bytesize_by_value = int(sys.getsizeof(list(range(int(1E7))))/1E7)
    cache_size = int(filesize / bytesize_by_value)

    store = ImmutableStore(location='./test_db/', avro_schema='data.v1.avsc', cache_size=cache_size, time_margin=datetime.timedelta(seconds=1))

    heartbeat = [-0.145,-0.145,-0.145,-0.145,-0.145,-0.145,-0.145,-0.145,-0.12,-0.135,-0.145,-0.15,-0.16,-0.155,-0.16,-0.175,-0.18,-0.185,-0.17,-0.155,-0.175,-0.18,-0.19,-0.18,-0.155,-0.135,-0.155,-0.19,-0.205,-0.235,-0.225,-0.245,-0.25,-0.26,-0.275,-0.275,-0.275,-0.265,-0.255,-0.265,-0.275,-0.29,-0.29,-0.29,-0.29,-0.285,-0.295,-0.305,-0.285,-0.275,-0.275,-0.28,-0.285,-0.305,-0.29,-0.3,-0.28,-0.29,-0.3,-0.315,-0.32,-0.335,-0.36,-0.385,-0.385,-0.405,-0.455,-0.485,-0.485,-0.425,-0.33,-0.22,-0.07,0.12,0.375,0.62,0.78,0.84,0.765,0.52,0.17,-0.165,-0.365,-0.435,-0.425,-0.37,-0.33,-0.325,-0.335,-0.345,-0.33,-0.325,-0.315,-0.31,-0.32,-0.335,-0.34,-0.325,-0.345,-0.335,-0.33,-0.335,-0.33,-0.325,-0.33,-0.33,-0.345,-0.355,-0.335,-0.325,-0.305,-0.32,-0.32,-0.33,-0.34,-0.335,-0.34,-0.345,-0.355,-0.355,-0.34,-0.33,-0.33,-0.33,-0.34,-0.35,-0.325,-0.325,-0.33,-0.33,-0.335,-0.335,-0.34,-0.33,-0.34,-0.35,-0.355,-0.35,-0.345,-0.33,-0.32,-0.335,-0.33,-0.345,-0.33,-0.335,-0.335,-0.345,-0.345,-0.355,-0.34,-0.34,-0.335,-0.33,-0.35,-0.35,-0.345,-0.335,-0.335,-0.335,-0.35,-0.355,-0.355,-0.345,-0.345,-0.335,-0.35,-0.36,-0.36,-0.36,-0.365,-0.36,-0.37,-0.385,-0.37,-0.36,-0.355,-0.36,-0.375,-0.375,-0.365,-0.365,-0.36,-0.36,-0.365,-0.37,-0.355,-0.33,-0.325,-0.325,-0.335,-0.34,-0.315,-0.3,-0.3,-0.29,-0.295,-0.29,-0.285,-0.275,-0.255,-0.25,-0.25,-0.265,-0.255,-0.245,-0.23,-0.245,-0.245,-0.255,-0.255,-0.24,-0.25,-0.255,-0.245,-0.255,-0.25,-0.25,-0.265,-0.26,-0.26,-0.265,-0.27,-0.265,-0.26,-0.275,-0.28,-0.29,-0.275,-0.27,-0.26,-0.28,-0.28,-0.285,-0.275,-0.275,-0.265,-0.27,-0.285,-0.29,-0.28,-0.275,-0.285,-0.28,-0.3,-0.3,-0.305,-0.295,-0.3,-0.31,-0.31,-0.305,-0.295,-0.285,-0.285,-0.29,-0.295,-0.31,-0.29,-0.295,-0.3,-0.305,-0.31,-0.325,-0.31,-0.3,-0.29,-0.31,-0.325,-0.33,-0.315,-0.3,-0.305,-0.31,-0.32,-0.33,-0.325,-0.315,-0.31,-0.305,-0.305,-0.31,-0.3,-0.305,-0.29,-0.3,-0.3,-0.305,-0.305,-0.29,-0.28,-0.295,-0.305,-0.315,-0.305,-0.295,-0.29,-0.28,-0.27,-0.275,-0.275,-0.27,-0.25,-0.25,-0.255,-0.225,-0.22,-0.205,-0.2,-0.205,-0.215,-0.23,-0.22,-0.225,-0.225,-0.225,-0.23,-0.235,-0.24,-0.235,-0.22,-0.21,-0.205,-0.245,-0.285,-0.285,-0.3,-0.31,-0.33,-0.33,-0.325,-0.315,-0.32,-0.315,-0.325,-0.34,-0.345,-0.34,-0.34,-0.35,-0.345,-0.355,-0.33,-0.335,-0.33,-0.32,-0.345,-0.355,-0.34,-0.33,-0.325,-0.33,-0.35,-0.365,-0.36,-0.38,-0.425,-0.445,-0.475,-0.51,-0.535,-0.505,-0.415,-0.3,-0.16,-0.015,0.235,0.49,0.72,0.875,0.94,0.905,0.755,0.49,0.165,-0.11,-0.27,-0.39,-0.45,-0.475,-0.455,-0.425,-0.39,-0.39,-0.385,-0.39,-0.38,-0.38,-0.38,-0.395,-0.385,-0.385,-0.385,-0.375,-0.395,-0.41,-0.41,-0.4,-0.395,-0.39,-0.405,-0.395,-0.385,-0.375,-0.39,-0.39,-0.405,-0.41,-0.41,-0.39,-0.39,-0.395,-0.405,-0.415,-0.4,-0.41,-0.405,-0.41,-0.415,-0.41,-0.4,-0.4,-0.395,-0.39,-0.405,-0.41,-0.39,-0.39,-0.385,-0.385,-0.41,-0.405,-0.395,-0.39,-0.375,-0.39,-0.395,-0.41,-0.4,-0.39,-0.39,-0.385,-0.405,-0.415,-0.415,-0.4,-0.395,-0.405,-0.415,-0.42,-0.42,-0.41,-0.415,-0.425,-0.42,-0.435,-0.43,-0.43,-0.42,-0.43,-0.45,-0.455,-0.45,-0.435,-0.445,-0.45,-0.455,-0.47,-0.46,-0.455,-0.45,-0.455,-0.47,-0.475,-0.46,-0.45,-0.445,-0.44,-0.435,-0.44,-0.41,-0.395,-0.37,-0.365,-0.36,-0.365,-0.34,-0.325,-0.315,-0.32,-0.33,-0.33,-0.32,-0.31,-0.3,-0.3,-0.32,-0.32,-0.315,-0.305,-0.305,-0.295,-0.32,-0.33,-0.305,-0.31,-0.3,-0.3,-0.32,-0.325,-0.31,-0.305,-0.315,-0.305,-0.315,-0.315,-0.31,-0.295,-0.29,-0.305,-0.31,-0.32,-0.315,-0.3,-0.315,-0.315,-0.315,-0.33,-0.315,-0.32,-0.315,-0.325,-0.335,-0.34,-0.335,-0.335,-0.33,-0.325,-0.345,-0.35,-0.345,-0.335,-0.33,-0.33,-0.345,-0.345,-0.345,-0.32,-0.33,-0.335,-0.34,-0.355,-0.335,-0.33,-0.33,-0.335,-0.355,-0.36,-0.355,-0.35,-0.34,-0.345,-0.345,-0.345,-0.345,-0.33,-0.33,-0.335,-0.345,-0.35,-0.35,-0.34,-0.33,-0.345,-0.345,-0.355,-0.35,-0.34,-0.33,-0.34,-0.34,-0.34,-0.33,-0.335,-0.33,-0.335,-0.345,-0.345,-0.34,-0.33,-0.315,-0.295,-0.3,-0.295,-0.285,-0.275,-0.265,-0.265,-0.265,-0.255,-0.25,-0.24,-0.225,-0.215,-0.24,-0.245,-0.24,-0.245,-0.235,-0.245,-0.25,-0.275,-0.275,-0.265,-0.25,-0.225,-0.22,-0.23,-0.265,-0.27,-0.28,-0.285,-0.305,-0.32,-0.34,-0.33,-0.335,-0.335,-0.355,-0.37,-0.36,-0.345,-0.35,-0.355,-0.365,-0.375,-0.38,-0.37,-0.365,-0.365,-0.38,-0.385,-0.38,-0.375,-0.355,-0.37,-0.39,-0.405,-0.41,-0.435,-0.465,-0.49,-0.52,-0.555,-0.57,-0.525,-0.405,-0.25,-0.09,0.12,0.41,0.69,0.885,0.96,0.85,0.52,0.05,-0.32,-0.5,-0.505,-0.445,-0.415]
    rp = RepeatPattern(heartbeat) # Seasonality
    rp += AutoincrementWithGenerator(0, Normal()) # Trend
    rp += Normal() # Noise




    while True:
        source_id = int(random.uniform(0, 20))
        type_id = int(random.uniform(0, 20))

        if random.uniform(0, 1) <= pctg_numerics:
            value = random.uniform(0, 180)
            store.write_lf(source_id=source_id, type_id=type_id, timestamp=dt_to_nano_timestamp(datetime.datetime.now()), value=value)
        else:
            freq = 125
            values = rp.get_batch(batch_size=freq).tolist()
            store.write_hf(source_id=source_id, type_id=type_id, start_date=dt_to_nano_timestamp(datetime.datetime.now()), frequency=freq, values=values)
        time.sleep(1.0/write_at)