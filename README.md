# Agente-Hippa
# 🛡️ Agente HIPAA (RAG)

Un agente de Inteligencia Artificial basado en la arquitectura **RAG (Retrieval-Augmented Generation)** diseñado para consultar la normativa legal y de privacidad de salud **HIPAA** (*Health Insurance Portability and Accountability Act*). 

El sistema procesa el documento oficial en inglés y permite a los usuarios hacer preguntas en español, obteniendo respuestas claras, precisas y fundamentadas en el texto legal sin necesidad de revisar las 25 páginas del documento manualmente.

---

## 🚀 ¿Qué hace el proyecto?

* **Procesamiento Multilingüe:** Lee y analiza el documento PDF oficial de HIPAA en inglés.
* **Consulta en Lenguaje Natural:** Permite realizar preguntas en español y devuelve respuestas en español claro y profesional.
* **Búsqueda Contextual (RAG):** Encuentra las secciones específicas del documento relevantes a la pregunta del usuario para evitar alucinaciones de la IA.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python
* **Orquestación de IA:** LangChain (usando LCEL - *LangChain Expression Language*)
* **Modelo de Lenguaje (LLM):** Google Gemini (`gemini-flash-latest`)
* **Modelo de Embeddings:** Google Gemini Embeddings (`gemini-embedding-001`)
* **Interfaz de Usuario:** Streamlit
* **Procesamiento de PDF:** `PyPDF`

---

## 📐 Arquitectura del Sistema

El flujo de trabajo del agente sigue el siguiente esquema:
