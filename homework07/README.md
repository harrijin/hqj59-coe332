# Homework 07

## A.

Deploy the Flask API and worker pods using the commands below:

```
kubectl apply -f ./deploy/api/harrijin-hw7-flask-deployment.yml
kubectl apply -f ./deploy/worker/harrijin-hw7-worker-deployment.yml
```

(Optional) Deploy the Flask service with the command below:

```
kubectl apply -f ./deploy/api/harrijin-hw7-flask-service.yml
```

Verify that the API and worker nodes are working properly with the following commands (and corresponding output) in a Python debug shell:

```
root@py-debug-deployment-5cc8cdd65f-kxsbc:/# curl -X POST -H "content-type: application/json" -d '{"start":1, "end":2}' 10.99.137.235:5000/jobs
{"id": "7b2fe63b-ad69-4ed9-b748-907208aac61d", "status": "submitted", "start": 1, "end": 2}

root@py-debug-deployment-5cc8cdd65f-kxsbc/# ipython
Python 3.9.2 (default, Mar 31 2021, 12:13:11) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.22.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import redis

In [2]: rd = redis.StrictRedis(host="10.101.245.196", port=6379, db
   ...: =0)

In [3]: rd.hgetall("job.7b2fe63b-ad69-4ed9-b748-907208aac61d")
Out[3]: 
{b'id': b'7b2fe63b-ad69-4ed9-b748-907208aac61d',
 b'status': b'done',
 b'start': b'1',
 b'end': b'2'}
```

## C.

`curl` commands to Flask API (10.99.137.235 is the IP address for my Flask service):

```
root@py-debug-deployment-5cc8cdd65f-kxsbc:/# curl -X POST -H "content-type: application/json" -d '{"start":1, "end":2}' 10.99.137.235:5000/jobs
{"id": "777dde5b-f8e6-451a-8109-ab7336d47f04", "status": "submitted", "start": 1, "end": 2}root@py-debug-deployment-5cc8cdd65f-kxsbc:/# curl -X POST -H "content-type: application/json" -d '{"start":1, "end":2}' 10.99.137.235:5000/jobs
{"id": "f4d5c9fe-2f24-4427-8828-e8baef8e3528", "status": "submitted", "start": 1, "end": 2}root@py-debug-deployment-5cc8cdd65f-kxsbc:/# curl -X POST -H "content-type: application/json" -d '{"start":1, "end":2}' 10.99.137.235:5000/jobs
{"id": "919abc95-b5ba-4165-8e9d-b9f719c2b16d", "status": "submitted", "start": 1, "end": 2}root@py-debug-deployment-5cc8cdd65f-kxsbc:/# curl -X POST -H "content-type: application/json" -d '{"start":1, "end":2}' 10.99.137.235:5000/jobs
{"id": "9b5d8a4d-22c0-4f9b-a009-d17ca56ead1b", "status": "submitted", "start": 1, "end": 2}root@py-debug-deployment-5cc8cdd65f-kxsbc:/# curl -X POST -H "content-type: application/json" -d '{"start":1, "end":2}' 10.99.137.235:5000/jobs
{"id": "4a63b5b3-c02a-4ad0-83f7-14a342d7ee69", "status": "submitted", "start": 1, "end": 2}root@py-debug-deployment-5cc8cdd65f-kxsbc:/# curl -X POST -H "content-type: application/json" -d '{"start":1, "end":2}' 10.99.137.235:5000/jobs
{"id": "a33ed53f-e773-4296-b364-47f3b56ca349", "status": "submitted", "start": 1, "end": 2}root@py-debug-deployment-5cc8cdd65f-kxsbc:/# curl -X POST -H "content-type: application/json" -d '{"start":1, "end":2}' 10.99.137.235:5000/jobs
{"id": "178958fc-73e6-46ec-b05d-639a7d04f3d7", "status": "submitted", "start": 1, "end": 2}root@py-debug-deployment-5cc8cdd65f-kxsbc:/# curl -X POST -H "content-type: application/json" -d '{"start":1, "end":2}' 10.99.137.235:5000/jobs
{"id": "9c74cab5-405e-4782-bea1-4c055f8bf502", "status": "submitted", "start": 1, "end": 2}root@py-debug-deployment-5cc8cdd65f-kxsbc:/# curl -X POST -H "content-type: application/json" -d '{"start":1, "end":2}' 10.99.137.235:5000/jobs
{"id": "c489d4d2-bd82-4dd1-ac97-3ffeceb2ce45", "status": "submitted", "start": 1, "end": 2}root@py-debug-deployment-5cc8cdd65f-kxsbc:/# curl -X POST -H "content-type: application/json" -d '{"start":1, "end":2}' 10.99.137.235:5000/jobs
{"id": "ec9d4760-fbc8-4b2c-bad2-db435c793ecf", "status": "submitted", "start": 1, "end": 2}
```

Python commands to check Redis database (after initializing `rd` the same way as in part A):

```
In [14]: rd.hgetall("job.777dde5b-f8e6-451a-8109-ab7336d47f04")
Out[14]: 
{b'id': b'777dde5b-f8e6-451a-8109-ab7336d47f04',
 b'status': b'done',
 b'start': b'1',
 b'end': b'2',
 b'worker': b'10.244.7.130'}

In [15]: rd.hgetall("job.f4d5c9fe-2f24-4427-8828-e8baef8e3528")
Out[15]: 
{b'id': b'f4d5c9fe-2f24-4427-8828-e8baef8e3528',
 b'status': b'done',
 b'start': b'1',
 b'end': b'2',
 b'worker': b'10.244.15.132'}

In [16]: rd.hgetall("job.919abc95-b5ba-4165-8e9d-b9f719c2b16d")
Out[16]: 
{b'id': b'919abc95-b5ba-4165-8e9d-b9f719c2b16d',
 b'status': b'done',
 b'start': b'1',
 b'end': b'2',
 b'worker': b'10.244.7.130'}

In [17]: rd.hgetall("job.9b5d8a4d-22c0-4f9b-a009-d17ca56ead1b")
Out[17]: 
{b'id': b'9b5d8a4d-22c0-4f9b-a009-d17ca56ead1b',
 b'status': b'done',
 b'start': b'1',
 b'end': b'2',
 b'worker': b'10.244.15.132'}

In [18]: rd.hgetall("job.4a63b5b3-c02a-4ad0-83f7-14a342d7ee69")
Out[18]: 
{b'id': b'4a63b5b3-c02a-4ad0-83f7-14a342d7ee69',
 b'status': b'done',
 b'start': b'1',
 b'end': b'2',
 b'worker': b'10.244.7.130'}

In [19]: rd.hgetall("job.a33ed53f-e773-4296-b364-47f3b56ca349")
Out[19]: 
{b'id': b'a33ed53f-e773-4296-b364-47f3b56ca349',
 b'status': b'done',
 b'start': b'1',
 b'end': b'2',
 b'worker': b'10.244.15.132'}

In [20]: rd.hgetall("job.178958fc-73e6-46ec-b05d-639a7d04f3d7")
Out[20]: 
{b'id': b'178958fc-73e6-46ec-b05d-639a7d04f3d7',
 b'status': b'done',
 b'start': b'1',
 b'end': b'2',
 b'worker': b'10.244.7.130'}

In [21]: rd.hgetall("job.9c74cab5-405e-4782-bea1-4c055f8bf502")
Out[21]: 
{b'id': b'9c74cab5-405e-4782-bea1-4c055f8bf502',
 b'status': b'done',
 b'start': b'1',
 b'end': b'2',
 b'worker': b'10.244.15.132'}

In [22]: rd.hgetall("job.c489d4d2-bd82-4dd1-ac97-3ffeceb2ce45")
Out[22]: 
{b'id': b'c489d4d2-bd82-4dd1-ac97-3ffeceb2ce45',
 b'status': b'done',
 b'start': b'1',
 b'end': b'2',
 b'worker': b'10.244.7.130'}

In [23]: rd.hgetall("job.ec9d4760-fbc8-4b2c-bad2-db435c793ecf")
Out[23]: 
{b'id': b'ec9d4760-fbc8-4b2c-bad2-db435c793ecf',
 b'status': b'done',
 b'start': b'1',
 b'end': b'2',
 b'worker': b'10.244.15.132'}
```

As shown by the output of the Python statements, each worker worked 5 jobs.