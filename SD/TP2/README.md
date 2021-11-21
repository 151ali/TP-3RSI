# Usage
```bash
docker-compose up
```
# Demo
go to http://localhost


![Demo](demo.gif)

# Tasks

## playing with Load‑Balancing algorithms
NGINX support the following load-balancing methods

## Round-Robin Load Balancing (the default)
```bash
upstream nginx-demo {
    server app1:5001;
    server app2:5002;
}
```

## Least Connections Load Balancing
```bash
upstream nginx-demo {
    least_conn;
    server app1:5001;
    server app2:5002;
}
```

## Least Time Load Balancing
```bash
upstream nginx-demo {
    least_time (header | last_byte);
    server app1:5001;
    server app2:5002;
}
```

## Random with Two Choices
```bash
upstream nginx-demo {
    server app1:5001;
    server app2:5002;
    random two; 
}
```

## Assigne weights
```bash
upstream nginx-demo {
    server app1:5001 weight=6; # 60%
    server app2:5002 weight=4; # 40%
}
```
app1 takes 6 requests

app2 takes 4 requests

## Connection Limiting
```bash
upstream nginx-demo {
    server app1:5001 max_conns=250;
    server app2:5002 max_conns=100;
}
```

## Ressources
21-11-2021

- [How to configure load balancing using Nginx](https://upcloud.com/community/tutorials/configure-load-balancing-nginx/)
- [NGINX and the “Power of Two Choices” Load-Balancing Algorithm](https://www.nginx.com/blog/nginx-power-of-two-choices-load-balancing-algorithm/)
- [Choosing an NGINX Plus Load-Balancing Technique](https://dzone.com/articles/choosing-an-nginx-plus-load-balancing-technique)
- [High-Performance Load Balancing](https://www.nginx.com/products/nginx/load-balancing/)
