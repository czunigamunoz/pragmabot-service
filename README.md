# PragmaBot ES

## ¡Hola!

Bienvenido a nuestro sistema de PragmaBot. Estamos encantados de tenerte aquí y esperamos brindarte toda la ayuda que necesitas.

## Descripción general del sistema

PragmaBot es una aplicación inteligente que utiliza una base de datos MongoDB para obtener el contexto necesario para sus interacciones. Está diseñado para brindar asistencia y generar alertas ante errores, advertencias o actividades inusuales.

El sistema se encuentra alojado en la nube y hace uso de tecnologías como AWS Lambda y CloudFront para garantizar la escalabilidad y disponibilidad del servicio. Gracias a esta infraestructura cloud, el bot puede manejar un gran número de solicitudes de manera eficiente.

## Comenzar

Estas instrucciones te permitirán obtener una copia del proyecto contenerizado en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

## Requerimientos recomendados

- **Docker y docker compose**: Debes asegurarte de tener Docker y docker compose instalados:
  - Windows o macOS: [Instalar Docker Desktop](https://www.docker.com/get-started/)
  - Linux: [Instalar Docker](https://www.docker.com/get-started/) y [docker-compose](https://docs.docker.com/compose/install/)
- **python:3.10.6-alpine**: Recomendamos utilizar python:3.10.6-alpine para garantizar la compatibilidad y el rendimiento óptimo. [Imagen de python official](https://hub.docker.com/_/python)

## Instalación

Para construir la aplicación, ejecuta el siguiente comando:

```bash
docker-compose up -d --build
```

Para entrar a la consola de la aplicación, ejecuta el siguiente comando:

```bash
docker-compose up
```

Para detener la aplicación, ejecuta el siguiente comando:

```bash
docker-compose down
```

¡Gracias por utilizar nuestro Asistente Bot! Si tienes alguna pregunta o necesitas ayuda adicional, no dudes en preguntar.

# PragmaBot EN

## Hello!

Welcome to our PragmaBot system. We are delighted to have you here and look forward to providing you with all the assistance you need.

## System Overview

PragmaBot is an intelligent application that uses a MongoDB database to obtain the necessary context for its interactions. It is designed to provide assistance and generate alerts for errors, warnings, or unusual activities.

The system is hosted in the cloud and makes use of technologies such as AWS Lambda and CloudFront to ensure scalability and availability of the service. Thanks to this cloud infrastructure, the bot can handle a large number of requests efficiently.


## Gettting started
These instructions will allow you to get a copy of the containerized project running on your local machine for development and testing purposes.

## Recommended Requirements

- **Docker and docker compose**: Make sure you have Docker and docker compose installed.:
  - Windows o macOS: [Install Docker Desktop](https://www.docker.com/get-started/)
  - Linux: [Install Docker](https://www.docker.com/get-started/) and [docker-compose](https://docs.docker.com/compose/install/)
- **python:3.10.6-alpine**: We recommend using python:3.10.6-alpine to ensure compatibility and optimal performance. [Imagen de python official](https://hub.docker.com/_/python)

## Installing

To build the application, run the following command:

```bash
docker-compose up -d --build
```

To enter the application console, run the following command:

```bash
docker-compose up
```

To stop the application, run the following command:

```bash
docker-compose down
```

This command will automatically install all the libraries and modules specified in the "requirements.txt" file, allowing the system to function smoothly, also, I'll create a virtual environment to separate the dependencies of this project with the others.

Thank you for using our Assistant Bot! If you have any questions or need further assistance, feel free to ask.
