# RCE (remote command executor)

Rce (remote command executor) is used to remotely control the host to execute commands.

### How to use it?

1. Create a log directory.

    ```bash
    mkdir -p /var/log/rce
    ```

2. Put the code in the `/root` directory.

3. Run the programme.

    ```bash
    python /root/rce/rce/main.py
    ```

4. Use the following command on the client to control the server to perform operations.

    - Execute a command.
    
        ```bash
        curl -X POST http://127.0.0.1:50201 -d 'ls -l'
        ```
    
    - Clear all processes that are executing.
    
        ```bash
        curl http://127.0.0.1:50201/clean
        ```
    
    > Replace `127.0.0.1` with the server address.
