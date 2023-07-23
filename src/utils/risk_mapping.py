def risk_mapping(risk: str):
    """
    Utility function created in order to map the risk category to a number.
    
    Baixo (Low) -> 0\n
    Médio (Medium) -> 1\n
    Alto (High) -> 2\n
    """
    risk_map: dict = {
        'Baixo': 0,
        'Médio': 1,
        'Alto': 2,
    }
    return risk_map.get(risk, 2) # 2 is the default value if the risk is not found in the map (Unknown risk)