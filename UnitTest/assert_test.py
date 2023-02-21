import pytest
import pyautogui

from PageObjectModel.Global_variables.Path_Data import PathAndVariablesUtil


def test_asser():
    try:
        a = "Hola mundo"
        b = "Hola soy german"
        assert a == b, "los textos no coinciden"
        print("los Textos son correctos")
        screenshot = pyautogui.screenshot()
        # Guardar imagen.
        screenshot.save(f"{PathAndVariablesUtil.db_path()}\\recursos\\screenshots\\Test\\screenshot.png")
    except:
        print("continua la prueba")

    c = "Continuacion"
    print(f"se mantiene {c} de la prueba")