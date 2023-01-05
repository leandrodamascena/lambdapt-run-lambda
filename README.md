sam build

sam deploy --guided

## Wrong output
```START RequestId: ad9cf05c-a102-4c4c-972f-b53188735b83 Version: $LATEST
{"level":"ERROR","location":"lambda_handler:8","message":"This will produce a structured log","timestamp":"2023-01-05 12:38:21,550+0000","service":"service_undefined","xray_trace_id":"1-63b6c4bd-7af914087a4dc33965a5de79"}
[ERROR] Exception: This will produce a unstructured log
Traceback (most recent call last):
  File "/var/task/app.py", line 10, in lambda_handler
    raise(Exception("This will produce a unstructured log"))END RequestId: ad9cf05c-a102-4c4c-972f-b53188735b83
REPORT RequestId: ad9cf05c-a102-4c4c-972f-b53188735b83	Duration: 17.20 ms	Billed Duration: 18 ms	Memory Size: 128 MB	Max Memory Used: 39 MB	Init Duration: 143.91 ms```
