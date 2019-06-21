# Локальная разработка

+ Активировать virtualenv (https://eax.me/python-virtualenv/)
+ Поставить зависимости 
  ```
  pip3 install -r requirements.txt
  ```
+ запустить приложение `python3 ./server.py`

# Docker

+ Сборка: `docker build -t python-server .`
+ Запуск: `docker-compose up -d`

# kubernetes/minikube

+ Деплой helm чарта (Изменить по потребности values.yaml)
```
helm install -n python-server . 
```

