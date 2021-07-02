# Container-dns

## Configure docker daemon
1.  Use the command  `sudo systemctl edit docker.service`  to open an override file for  `docker.service`  in a text editor.
2.  Add or modify the following lines, substituting your own values.  
    ```systemd
    [Service]
    ExecStart=
    ExecStart=/usr/bin/dockerd -H fd:// -H tcp://127.0.0.1:2375
    ```
3.  Reload the  `systemctl`  configuration.
    ```
     $ sudo systemctl daemon-reload
    ```
5.  Restart Docker.
    ```
    $ sudo systemctl restart docker.service
    ```
