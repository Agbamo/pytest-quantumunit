def test_plugin_loaded(pytestconfig):
    """Verifica qué plugins están registrados"""
    plugins = pytestconfig.pluginmanager.list_name_plugin()
    print(f"Plugins registrados: {plugins}")  # Depuración
    
    # Verificamos si el nombre del plugin aparece en la lista
    assert any("quantumunit" in p[0] for p in plugins), f"Plugins registrados: {plugins}"