def convertir_fecha(fecha):
    """Función que convierte una fecha en formato MM/DD/AAAA o 'Mes día, año' al formato AAAA-MM-DD."""

    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    if '/' in fecha:  
        mes, dia, año = fecha.split('/')
    else:  
        partes = fecha.replace(',', '').split()
        mes = str(meses.index(partes[0]) + 1).zfill(2)  
        dia = partes[1].zfill(2)
        año = partes[2]

    mes = mes.zfill(2)
    dia = dia.zfill(2)

    fecha_formateada = f"{año}-{mes}-{dia}"
    return fecha_formateada

fecha_input = input("Ingrese una fecha (formato MM/DD/AAAA o 'Mes día, año'): ")

fecha_output = convertir_fecha(fecha_input)
print(f"Fecha en formato AAAA-MM-DD: {fecha_output}")
