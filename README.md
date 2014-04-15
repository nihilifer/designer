The most current
================
```
git submodule update --init
vagrant up
```

And server is running. If you want to restart server do:
```
vagrant ssh
restart
exit
```

There will be two apps running:
- with nginx and /usr/bin/shmir (generated by setup.py) on port 8080 - http://127.0.0.1:8080/
- development instance on port 8090 (launched directly from currently existing code) - http://127.0.0.1:8090/

curl examples to test:

```
curl -i -X POST -H 'Content-Type: application/json; charset=utf-8' -d '{"data": "UTGCCAAA"}' http://127.0.0.1:8080/mfold
curl -i -X POST -H 'Content-Type: application/json; charset=utf-8' -d '{"data": "UTGCCAAA"}' http://127.0.0.1:8090/mfold
```
