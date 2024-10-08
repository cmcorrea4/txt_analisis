import subprocess

def descargar_corpora():
    try:
        # Ejecutar el comando "python -m textblob.download_corpora"
        subprocess.run([f"{sys.executable}", "-m", "textblob.download_corpora"], check=True)
        print("Corpora descargados correctamente.")
    except subprocess.CalledProcessError:
        print("Error al descargar los corpora.")

if __name__ == "__main__":
    descargar_corpora()
