import main

def test_abrir_conexion_existe():
    at_main = dir(main)
    assert "abrir_conexion" in at_main

def test_abrir_conexion():
    conn = main.abrir_conexion()
    assert conn
