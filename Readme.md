# Agente RAG Visual con FiftyOne

**IA Agéntica + RAG Visual** para productos de consumo masivo  
Sistema inteligente que ve, recupera y razona sobre imágenes con ayuda de embeddings visuales y agentes LLM.

---

##  Descripción

Este proyecto implementa un agente visual inteligente que:

- Recibe imágenes de productos de consumo
- Genera embeddings visuales con [CLIP](https://openai.com/research/clip)
- Recupera productos similares desde una base vectorial (Pinecone)
- Usa un LLM (OpenAI o similar) para aplicar filtros y razonamiento contextual
- Visualiza resultados y metadata usando [FiftyOne](https://voxel51.com/fiftyone)

> 🔍 Pensado para aplicaciones en e-commerce, comparadores visuales.

---

## Arquitectura

``` flowchart LR
    A[Imagen de entrada] --> B[Embedding con CLIP]
    B --> C[Consulta a Pinecone]
    C --> D[LangChain Agent + LLM]
    D --> E[Respuesta enriquecida]
    E --> F[FiftyOne: Visualización]
```