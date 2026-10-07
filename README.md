# 💇‍♀️ Sistema de Gestión para Salón de Belleza

## 📌 Descripción

Este repositorio contiene el desarrollo de un sistema de gestión para un salón de belleza, realizado como proyecto académico de la materia **Programación Orientada a Objetos**.

El sistema será desarrollado en **Python** y permitirá aplicar los principales conceptos de la POO mediante la gestión de clientes, empleados, servicios y citas.

---

## 🎯 Objetivo

Desarrollar un sistema que permita gestionar las principales actividades de un salón de belleza, aplicando los conceptos de Programación Orientada a Objetos y organizando el código mediante módulos y paquetes.

---

## 📁 Estructura del proyecto

El proyecto está organizado mediante paquetes y módulos, con el propósito de separar las diferentes responsabilidades del sistema.

```text
Sistema-salon-belleza/
│
├── modelos/
│   └── cliente.py
│
├── servicios/
│   └── gestion_citas.py
│
├── main.py
└── README.md
```

📦 Paquete modelos
Este paquete contendrá las clases que representan las principales entidades del salón de belleza, como clientes, empleados, servicios y citas.
Actualmente contiene:
- cliente.py: módulo destinado a la representación y gestión de la información de los clientes.

📦 Paquete servicios
Este paquete contendrá la lógica necesaria para realizar las diferentes operaciones del sistema.
Actualmente contiene:
- gestion_citas.py: módulo destinado a las operaciones relacionadas con la programación y gestión de citas.

🐍 main.py
Es el archivo principal del proyecto. Será el punto de inicio de la aplicación y permitirá utilizar los diferentes módulos y paquetes que conforman el sistema.

⚙️ Funcionalidades previstas
- 👩 Gestión de clientes.
- 💇 Gestión de empleados.
- ✂️ Gestión de servicios ofrecidos por el salón.
- 📅 Registro y gestión de citas.
- 🔎 Consulta de información de clientes y citas.

🛠️ Tecnologías y herramientas
- Python
- Programación Orientada a Objetos
- Git
- GitHub
