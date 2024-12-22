# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos al contenedor
COPY requirements.txt requirements.txt
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el script de inicio
COPY start.sh start.sh
RUN chmod +x start.sh

# Expone el puerto 8080 para Flask
EXPOSE 8080

# Comando para iniciar ambos servicios
CMD ["./start.sh"]
