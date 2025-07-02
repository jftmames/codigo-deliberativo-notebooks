# Código Deliberativo - Librerías `deliberative_core`

Este repositorio contiene el paquete de librerías `deliberative_core`, un sistema modular en Python diseñado para facilitar procesos de razonamiento estructurado y deliberación asistida por IA. El sistema permite descomponer preguntas complejas, registrar el flujo de pensamiento y evaluar la calidad del proceso deliberativo mediante el Índice de Equilibrio Erotético (EEE).

Este proyecto cumple con los requisitos del **Plan Maestro para el Desarrollo de Librerías**.

---

## ✅ Características Principales

* **Motor de Indagación (`inquiry_engine`)**: Utiliza modelos de lenguaje grandes (como los de OpenAI) para generar subpreguntas y explorar temas en profundidad.
* **Trazador de Razonamiento (`reasoning_tracker`)**: Registra cada paso del proceso (preguntas, respuestas) como un nodo en un árbol de razonamiento, garantizando una trazabilidad epistémica completa.
* **Navegador (`navigator`)**: Orquesta el flujo deliberativo, gestionando las rutas de exploración y el estado de cada pregunta.
* **Módulo de Evaluación (`eee`)**: Calcula métricas de calidad como la **profundidad** y la **pluralidad** del árbol de razonamiento.

---

## 🚀 Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/jftmames/codigo-deliberativo-notebooks.git](https://github.com/jftmames/codigo-deliberativo-notebooks.git)
    cd codigo-deliberativo-notebooks
    ```

2.  **Instalar las dependencias:**
    Se recomienda crear un entorno virtual primero.
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Configurar la API Key de OpenAI:**
    Crea un archivo llamado `.env` en la raíz del proyecto y añade tu clave de API:
    ```
    OPENAI_API_KEY='tu_clave_secreta_aqui'
    ```
    Este archivo es ignorado por Git para proteger tu clave.

---

## 💡 Cómo Usarlo

El archivo `main_simulation.py` contiene un ejemplo completo que muestra cómo usar las librerías. Para ejecutarlo:

```bash
python main_simulation.py
```

Esto iniciará un proceso deliberativo, explorará una pregunta principal y una subpregunta, y finalmente imprimirá en la terminal tanto las métricas de evaluación (EEE) como el historial completo del razonamiento en formato JSON.

---

## 🧪 Pruebas

El proyecto incluye una suite de pruebas automáticas. Para ejecutarlas, asegúrate de haber instalado las dependencias de desarrollo y luego corre:

```bash
pytest
```