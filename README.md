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

[ PDF de HIPAA (Inglés) ] → [ Carga y Chunking (RecursiveCharacterTextSplitter) ] → [ Embeddings (gemini-embedding-001) ] → [ Almacén Vectorial en Memoria (DocArrayInMemorySearch) ] → [ Recuperación de Contexto (Retrieval) ] → [ Generación de Respuesta con LCEL + Gemini (Español) ] → [ Interfaz de Usuario (Streamlit) ]

---

## 💬 Ejemplos de Preguntas y Respuestas

### Ejemplo 1:
* **Pregunta:** ¿Qué se considera Información de Salud Protegida (PHI) según el documento?
* **Respuesta:** La PHI (Protected Health Information) abarca cualquier información de salud individualmente identificable transmitida o mantenida por una entidad cubierta. Incluye datos demográficos, historial médico pasado, presente o futuro, provisión de atención médica y detalles de pago que puedan identificar al individuo (como nombre, dirección, fecha de nacimiento o número de Seguro Social).

### Ejemplo 2:
* **Pregunta:** ¿Cuáles son las excepciones para compartir información de salud sin la autorización explícita del paciente?
* **Respuesta:** Según la normativa HIPAA, la información se puede divulgar sin autorización expresa en situaciones específicas como: tratamiento médico, pago de servicios, operaciones de atención médica, actividades de interés y beneficio público (salud pública, víctimas de abuso o negligencia, investigaciones judiciales, cumplimiento de la ley) o en situaciones de emergencia para prevenir una amenaza seria a la salud o seguridad.

---
