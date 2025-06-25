# 🔍 Escáner de Red Local Estilo Hacker — by Code Hers

¡Aprende ciberseguridad básica creando tu propio escáner de red con Python, Nmap y Scapy!  
Este proyecto te guía paso a paso a construir una herramienta que detecta dispositivos conectados y escanea puertos abiertos en tu red local, como lo haría un hacker ético.  
Ideal para estudiantes, entusiastas de redes y futuros pentesters.  

> ⚠️ **Solo para fines educativos. No escanees redes ajenas sin permiso.**

---

## 🧠 ¿Qué aprenderás?

- Cómo funciona una red local
- Qué es un puerto y cómo escanearlo
- Fundamentos de Nmap y Scapy en Python
- Crear herramientas de hacking ético reales
- Buenas prácticas en desarrollo con entornos virtuales

---

## ✅ Requisitos

- Python 3.8 o superior
- Sistema operativo Windows, Linux o macOS
- Acceso a una red local (Wi-Fi o Ethernet)
- Permisos de administrador si deseas hacer escaneos SYN (`-sS`)
- Instalación de [Nmap](https://nmap.org/download.html)

---

## ⚙️ Instalación paso a paso
# En Windows
py -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install python-nmap scapy
pip freeze > requirements.txt
nmap --version


### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/scaner-hacker.git
cd scaner-hacker
