# flask-redis-counter-practica-ramon-meza

## Descripción y Función del Proyecto
**Flask-Redis-Counter** es una aplicación web sencilla desarrollada con Flask (Python) que implementa un contador persistente utilizando Redis como base de datos en memoria.  
El objetivo de esta aplicación es ofrecer un ejemplo funcional y educativo sobre cómo desarrollar y contenerizar una aplicación web con persistencia simple, sin necesidad de una base de datos relacional.

## Estructura del Proyecto Completa

```plaintext
FLASK-REDIS-COUNTER-PRACTICA-RAMONMEZA/
│
├── app/                         # Código fuente principal
│   ├── __init__.py
│   ├── main.py
│   ├── redis_client.py
│   └── templates/
│       └── index.html
│
├── tests/                       # Pruebas unitarias
│   └── test_redis.py
│
├── k8s/                         # Manifiestos de Kubernetes
│   ├── configmap.yaml           # Configuración de variables de entorno para la app
│   ├── deployment.yaml          # Despliegue de Flask en Kubernetes
│   ├── pvc.yaml                 # Volumen persistente para almacenamiento
│   ├── redis-deployment.yaml   # Despliegue de Redis
│   ├── redis-service.yaml      # Servicio para exponer Redis internamente
│   ├── secret.yaml             # Secretos para la aplicación (como SECRET_KEY)
│   └── service.yaml            # Servicio para exponer la app Flask
│
├── .circleci/                   # Configuración de CI/CD con CircleCI
│   └── config.yml
│
├── Dockerfile                   # Imagen Docker para la app Flask
├── docker-compose.yml           # Orquestación local: Flask + Redis
├── requirements.txt             # Dependencias de Python
├── README.md                    # Documentación del proyecto
├── .gitignore                   # Archivos ignorados por Git
└── venv/                        # Entorno virtual de Python (opcional)

```

## Proyecto Flask-Redis-Counter

Este repositorio contiene los manifiestos de Kubernetes y la configuración necesaria para desplegar una aplicación Flask que interactúa con Redis. La aplicación se usa como un contador, y todos los componentes están desplegados de manera eficiente utilizando Kubernetes.

## Qué realiza cada manifiesto dentro de k8s/

A continuación se describe el propósito de cada uno de los archivos dentro del directorio `k8s/`:

- **`deployment.yaml`**: Despliega la aplicación Flask en un Deployment con múltiples réplicas para garantizar alta disponibilidad y escalabilidad.
- **`service.yaml`**: Expone la aplicación Flask como un Service dentro del clúster, utilizando el tipo adecuado (ClusterIP o NodePort) para la accesibilidad.
- **`configmap.yaml`**: Define variables de entorno no sensibles, tales como configuraciones de la aplicación que no contienen información sensible.
- **`secret.yaml`**: Define secretos como claves de la aplicación o credenciales que deben ser almacenadas de forma segura y se usen como variables de entorno.
- **`pvc.yaml`**: Crea un PersistentVolumeClaim (PVC) para almacenamiento persistente de datos que la aplicación Flask y Redis puedan necesitar.
- **`redis-deployment.yaml`**: Despliega Redis en un contenedor separado para el almacenamiento en memoria y manejo de datos.
- **`redis-service.yaml`**: Expone Redis como un servicio interno en el clúster para ser accesible por la aplicación Flask.

## Clonar el Proyecto

Para comenzar, clona este repositorio ejecutando el siguiente comando:

```bash
git clone git@github.com:RAMON1743/flask-redis-counter-Practica-RamonMeza.git

```

## Ejecutamos localmente con Docker

```bash
docker-compose up --build
```

Una vez que los contenedores se hayan construido y estén corriendo, podrás acceder a la aplicación Flask en la siguiente dirección:

http://localhost:5000
