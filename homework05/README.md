# Homework 05 Submission

This directory contains my submission for homework 5.

## Part A

Command to create pod:

```
kubectl apply -f greeting-pod-A.yml
```

The output was unexpected because the $NAME environment variable is empty.

Command to delete pod:

```
kubectl delete pods hello
```

## Part B

Command to create pod:
```
kubectl apply -f greeting-pod-B.yml
```

Command to get log:
```
kubectl logs hello
```

Output:
```
Hello, Harrison!
```

Command to delete pod:
```
kubectl delete pods hello
```

## Part C

Command to create deployment:
```
kubectl apply -f greeting-deployment.yml
```

Command to get pods and IP addresses:
```
kubectl get pods -o wide
```

Output of above command:
```
NAME                                              READY   STATUS    RESTARTS   AGE     IP             NODE   NOMINATED NODE   READINESS GATES
greeting-deployment-667799555c-k9f65              1/1     Running   0          3m12s   10.244.7.101   c05    <none>           <none>
greeting-deployment-667799555c-mpr6w              1/1     Running   0          3m12s   10.244.5.103   c04    <none>           <none>
greeting-deployment-667799555c-rrdlk              1/1     Running   0          3m12s   10.244.3.96    c01    <none>           <none>
```

Checking logs of pods:
```
$ kubectl logs greeting-deployment-667799555c-k9f65
Hello, Harrison from IP 10.244.7.101!
$ kubectl logs greeting-deployment-667799555c-mpr6w
Hello, Harrison from IP 10.244.5.103!
$ kubectl logs greeting-deployment-667799555c-rrdlk
Hello, Harrison from IP 10.244.3.96!
```