# ⚡ Fzn - Fast Fuzzing Tool

![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Ruby Version](https://img.shields.io/badge/Ruby-3.x-red?style=for-the-badge&logo=ruby)
![Status](https://img.shields.io/badge/Status-In_Development-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
```text
  ███████╗███████╗███╗   ██╗
  ██╔════╝╚══███╔╝████╗  ██║
  █████╗    ███╔╝ ██╔██╗ ██║
  ██╔══╝   ███╔╝  ██║╚██╗██║
  ██║     ███████╗██║ ╚████║
  ╚═╝     ╚══════╝╚═╝  ╚═══╝ v1.0
 Fast Fuzzing Tool by ThAx2
```

**Fzn** es una herramienta de Fuzzing de nueva generación. A diferencia de otros fuzzers, Fzn combina la potencia de **Python** para la ejecución concurrente con la flexibilidad de **Ruby** para la manipulación dinámica de datos.

## 🚀 ¿Por qué Fzn?

*   **Target Analysis (Pre-Attack):** No dispares a ciegas. Fzn analiza IP, Servidor, WAF, Títulos y Redirecciones antes de iniciar el fuzzing.
*   **Arquitectura Híbrida:** Núcleo de red en Python y motores de permutación de payloads en Ruby.
*   **Placeholder `$fzn`:** Control total sobre dónde inyectar el diccionario (rutas, parámetros o extensiones).
*   **Evasión Integrada:** Rotación de `User-Agent` y soporte para Proxies (HTTP/SOCKS).

---

## 📸 Demo Visual

![Análisis de Target y Banner](image_b1f233.png)

---

## 🛠️ Instalación

1. Clona el repositorio:
```bash
git clone [https://github.com/ThAx2/Fzn.git](https://github.com/ThAx2/Fzn.git)
cd Fzn
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```
*(Se requiere Python 3.10+ y Ruby instalado para módulos de permutación).*

---

## 📖 Uso

```bash
python3 fzn.py -u [https://target.com](https://target.com) -w common.txt
```

### Opciones Avanzadas

| Parámetro | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `-u`, `--url` | URL del objetivo (Obligatorio) | `-u https://target.com` |
| `-w`, `--wordlist` | Ruta del diccionario | `-w common.txt` |
| `-t`, `--thread` | Hilos simultáneos (Default: 5) | `-t 50` |
| `-p`, `--proxy` | Enrutar por Proxy | `-p 127.0.0.1:9050` |

---

## ⚠️ Aviso Legal (Disclaimer)

Esta herramienta fue creada con fines estrictamente educativos y para su uso en entornos autorizados. El autor (**ThAx2**) no se hace responsable del mal uso ni de los daños causados. **Úsala bajo tu propia responsabilidad.**
