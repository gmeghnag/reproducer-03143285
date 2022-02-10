## reproducer-03143285
---

### Run reproducer
It runs a pod (single container) who output sized chunk logs as expressed by the `BYTES` env variable.
```
oc run reproducer-03143285  --image=quay.io/gmeghnag/reproducer-03143285 --env="BYTES=30972802" --env="SLEEP=40"
```

### Get node were reproducer is running
```
NODE=$(oc get pods -A -l run=reproducer-03143285 -o jsonpath='{.items[0].spec.nodeName}')
```

### Get the name of the fluentd who is collecting the  reproducer logs
```
oc get pods -n openshift-logging -l 'component in (fluentd, collector)' -o jsonpath="{.items[?(@.spec.nodeName=='$NODE')].metadata.name}"
```

### Catch `BufferChunkOverflowError` error
```
oc logs -n openshift-logging $(oc get pods -n openshift-logging -l 'component in (fluentd, collector)' -o jsonpath="{.items[?(@.spec.nodeName=='$NODE')].metadata.name}") --all-containers | grep BufferChunkOverflowError | head -1
```
---
### Workaround
Increase chunck limit size from fluentd [1].


[1] https://docs.openshift.com/container-platform/4.7/logging/config/cluster-logging-collector.html#cluster-logging-collector-tuning_cluster-logging-collector