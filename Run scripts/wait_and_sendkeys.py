import pyautogui
import time
import sys
import os

# --- Configuración ---
# Nombre del archivo de imagen que indica que PAD está listo
READY_IMAGE_FILENAME = "pad_ready_indicator.png"
# Tiempo máximo de espera en segundos para encontrar la imagen
MAX_WAIT_SECONDS = 60
# Intervalo entre búsquedas de imagen (en segundos)
POLL_INTERVAL_SECONDS = 2
# Confianza para la búsqueda de imágenes (0.0 a 1.0)
IMAGE_CONFIDENCE = 0.8
# Título de la ventana de Power Automate (ajústalo si es diferente en tu idioma/versión)
PAD_WINDOW_TITLE = "Power Automate"
# --- Fin de la Configuración ---

def wait_for_pad_ready():
    """Espera hasta que la imagen indicadora sea visible en pantalla."""
    print(f"Esperando a que '{READY_IMAGE_FILENAME}' aparezca (max {MAX_WAIT_SECONDS} seg)...")

    start_time = time.time()
    while time.time() - start_time < MAX_WAIT_SECONDS:
        try:
            location = pyautogui.locateOnScreen(READY_IMAGE_FILENAME, confidence=IMAGE_CONFIDENCE)
            if location:
                print(f"'{READY_IMAGE_FILENAME}' encontrada en {location}. PAD parece listo.")
                return True
            else:
                # Imagen no encontrada aún, esperar antes de volver a buscar
                print(".", end="", flush=True) # Indicador de progreso
                time.sleep(POLL_INTERVAL_SECONDS)

        except pyautogui.PyAutoGUIException as e:
            print(f"\nError de PyAutoGUI durante la búsqueda: {e}")
            # Podría ser un problema de permisos o acceso a la pantalla
            time.sleep(POLL_INTERVAL_SECONDS)
        except Exception as e:
            print(f"\nError inesperado durante la búsqueda: {e}")
            time.sleep(POLL_INTERVAL_SECONDS)

    print(f"\nERROR: Tiempo de espera agotado ({MAX_WAIT_SECONDS} seg). No se encontró '{READY_IMAGE_FILENAME}'.")
    return False

def activate_pad_and_send_keys():
    """Intenta activar la ventana de PAD y envía la combinación de teclas."""
    print(f"Intentando activar la ventana con título '{PAD_WINDOW_TITLE}'...")
    try:
        # Obtener todas las ventanas con ese título (podría haber más de una)
        pad_windows = pyautogui.getWindowsWithTitle(PAD_WINDOW_TITLE)
        if not pad_windows:
            print(f"ADVERTENCIA: No se encontró ninguna ventana con el título '{PAD_WINDOW_TITLE}'.")
            # Intentar enviar teclas de todos modos, podría funcionar si ya está activa
        else:
            # Intentar activar la primera ventana encontrada
            pad_window = pad_windows[0]
            try:
                if pad_window.isMinimized:
                    pad_window.restore()
                pad_window.activate()
                print("Ventana activada (o intento realizado). Esperando un momento...")
                time.sleep(1) # Pequeña pausa después de activar
            except Exception as e:
                 print(f"ADVERTENCIA: No se pudo activar la ventana '{PAD_WINDOW_TITLE}'. Error: {e}")
                 print("Intentando enviar teclas de todos modos...")

        # Enviar la combinación de teclas Ctrl+Alt+Shift+B
        print("Enviando teclas: Ctrl+Alt+Shift+B")
        pyautogui.hotkey('ctrl', 'alt', 'shift', 'b')
        print("Combinación de teclas enviada.")
        return True

    except Exception as e:
        print(f"ERROR al intentar activar la ventana o enviar teclas: {e}")
        return False

# --- Ejecución Principal ---
if __name__ == "__main__":
    # Verificar si existe el archivo de imagen
    if not os.path.exists(READY_IMAGE_FILENAME):
        print(f"ERROR FATAL: El archivo de imagen '{READY_IMAGE_FILENAME}' no se encuentra.")
        print("Asegúrate de haber capturado la imagen y guardado en la misma carpeta que este script.")
        sys.exit(1) # Salir con código de error

    # 1. Esperar a que PAD esté visualmente listo
    if wait_for_pad_ready():
        # 2. Activar ventana y enviar teclas
        time.sleep(1) # Una pequeña pausa extra por si acaso la UI se está terminando de dibujar
        if activate_pad_and_send_keys():
            print("Script Python completado con éxito.")
            sys.exit(0) # Salir con código de éxito
        else:
            print("Script Python falló al enviar las teclas.")
            sys.exit(1) # Salir con código de error
    else:
        print("Script Python falló porque PAD no pareció cargar a tiempo.")
        sys.exit(1) # Salir con código de error