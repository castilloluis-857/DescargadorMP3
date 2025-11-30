import yt_dlp
import os
import tkinter as tk
import shutil

def descargar_mp3():
    url = entrada_url.get()
    if not url:
        etiqueta_mensaje.config(text="⚠️ Por favor introduce una URL", fg="red")
        return

    carpeta_usuario = os.path.expanduser("~")
    carpeta_musica = os.path.join(carpeta_usuario, "Music")
    carpeta_descargas = os.path.join(carpeta_usuario, "Downloads")

    opciones = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(carpeta_musica, '%(title)s.%(ext)s')
    }

    try:
        etiqueta_mensaje.config(text="⏳ Descargando...", fg="blue")
        ventana.update_idletasks()

        with yt_dlp.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=True)
            nombre_archivo = ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3")

        # Copiar a Descargas
        destino = os.path.join(carpeta_descargas, os.path.basename(nombre_archivo))
        shutil.copy(nombre_archivo, destino)

        etiqueta_mensaje.config(
            text=f"✅ MP3 guardado en:\n🎵 Música y 📥 Descargas", fg="green"
        )
    except Exception as e:
        etiqueta_mensaje.config(text=f"❌ Error: {e}", fg="red")

# Interfaz
ventana = tk.Tk()
ventana.title("Descargador MP3")
ventana.geometry("450x200")

tk.Label(ventana, text="Introduce la URL del video:").pack(pady=10)
entrada_url = tk.Entry(ventana, width=50)
entrada_url.pack(pady=5)

tk.Button(ventana, text="Descargar MP3", command=descargar_mp3).pack(pady=10)
etiqueta_mensaje = tk.Label(ventana, text="", fg="black")
etiqueta_mensaje.pack(pady=10)

ventana.mainloop()
