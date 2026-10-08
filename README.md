# Unified Async LLM Client

Cliente asíncrono y unificado para interactuar con modelos de OpenAI y Anthropic mediante una interfaz común basada en Python 3.12 y Pydantic.

## Requisitos Previos

- Python 3.12 instalado.
- API Keys activas de OpenAI y/o Anthropic.

## Instalación y Configuración

1. Clonar el repositorio y navegar a la carpeta raíz.
2. Crear y activar el entorno virtual:
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate  # Mac / Linux
   pip install -r requirements.txt
   cp .env.example .env