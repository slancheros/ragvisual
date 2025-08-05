
from transformers import CLIPProcessor, CLIPModel
from huggingface_hub import login
import os

# Opcional: usar token para acceso autenticado si es necesario
hf_token = os.getenv("HUGGINGFACE_HUB_TOKEN")
if hf_token:
    login(token=hf_token)

# Descargar y guardar modelo y procesador en ./model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32", trust_remote_code=False)
model.save_pretrained("./model")

processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
processor.save_pretrained("./model")