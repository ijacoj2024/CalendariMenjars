import requests
from datetime import datetime

# ⚙ CONFIGURA AQUÍ
TOKEN = "8270414353:AAGTDR3c3NruthuVu-pd4WXT5UPtRyFj9Ik"        # Token de tu bot de Telegram
CHAT_ID = "762111685"    # Chat ID que obtuviste

def enviar_receta():
    receta = {
        "titulo": "Ensalada Mediterránea rápida",
        "descripcion": "Fresca, saludable y lista en 15 minutos. Ideal para 4 personas.",
        "imagen": "https://i.imgur.com/4N6pC1h.jpg",
        "link": "https://www.recetas.com/ensalada-mediterranea"
    }

    mensaje = f"*{receta['titulo']}*\n{receta['descripcion']}\n[Ver receta]({receta['link']})"

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
        data={"chat_id": CHAT_ID, "caption": mensaje, "parse_mode": "Markdown"},
        files={"photo": requests.get(receta["imagen"]).content}
    )

if __name__ == "__main__":
    enviar_receta()
