# Pancarte DB

## How it works

### What does it stores?

Immutable data:

* Raw waveforms (high frequency data, does not stores timestamps for each value, needs constant frequency data)
* Numerics (low frequency data, stores a value with a timestamp)
* Metadata such as source_id, type_id...

Mutable data:

* Annotation types
* Timestamp-based annotations
* Timerange-based annotations


### What can it do?

Writes:

* [x] Write waveforms, numerics
* [x] Write annotations

Read (you can combine these options):

* [x] Get data from date A to date B
* [ ] Get data where record_length >= 2hours
* [x] Get data where bed_id=X, signal_type=ECG
* [ ] Get data where there are arythmia annotations


### How does it stores data?

There are two types of data:

* Immutable: waveforms and numerics
* Editable/Expandable: metadata and annotations

Immutable data is directly stored in files that are not supposed to be editable.
Editable/Expandable data is stored in an easily queryable store (sqlite).

![alt text](architecture.png)

## Running it

```
python3 api.py hostname port
```


## Using it

### Annotations types:

An annotation type might be like 'bradycardia arrhythmia', 'start of record', 'end of record', 'heart R peak' or whatever you'd like

* GET on <api-url>/annotations/types -> returns all the annotations types
* GET on <api-url>/annotations/types/<id> -> returns the annotation type where id=<id>
* POST on <api-url>/annotations/types (parameters=name:string) -> returns the created annotation type with http code 201
* PUT on <api-url>/annotations/types/<id> (parameters=name:string) -> updates the annotation type where id=<id> and returns it
* DELETE on <api-url>/annotations/types/<id> -> deletes the annotation type where id=<id> and returns http code 204

### Timestamp-based Annotations:

* GET on <api-url>/annotations/timestamp -> returns all the annotations that are timestamp-based
* GET on <api-url>/annotations/timestamp/<id> -> returns the annotation where id=<id>
* POST on <api-url>/annotations/timestamp (parameters=source_id:int, type_id:int, value:float, comment:string, timestamp_micros:int) -> returns the created annotation with http code 201
* PUT on <api-url>/annotations/timestamp/<id> (parameters=source_id:int, type_id:int, value:float, comment:string, timestamp_micros:int) -> updates the annotation where id=<id> and returns it
* DELETE on <api-url>/annotations/timestamp/<id> -> deletes the annotation where id=<id> and returns http code 204

### Timerange-based Annotations:

* GET on <api-url>/annotations/timerange -> returns all the annotations that are timerange-based
* GET on <api-url>/annotations/timerange/<id> -> returns the annotation where id=<id>
* POST on <api-url>/annotations/timerange (parameters=source_id:int, type_id:int, values:float, comment:string, start_micros:int, end_micros:int) -> returns the created annotation with http code 201
* PUT on <api-url>/annotations/timerange/<id> (parameters=source_id:int, type_id:int, values:float, comment:string, start_micros:int, end_micros:int) -> updates the annotation where id=<id> and returns it
* DELETE on <api-url>/annotations/timerange/<id> -> deletes the annotation where id=<id> and returns http code 204

