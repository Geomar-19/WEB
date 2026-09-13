from django.db import models

class Recurso(models.Model):
    # Definimos las categorías de tu contenido
    OPCIONES_CATEGORIA = [
        ('TRADING', 'Trading e Indicadores MT5'),
        ('FISCAL', 'Ciencias Fiscales y Aranceles'),
        ('YOUTUBE', 'Recursos de YouTube / Edición'),
    ]

    titulo = models.CharField(max_length=200, help_text="Ej: Bot MQL5, Calculadora de Aranceles")
    descripcion = models.TextField(help_text="Explica para qué sirve o cómo usarlo.")
    categoria = models.CharField(max_length=20, choices=OPCIONES_CATEGORIA, default='TRADING')
    archivo = models.FileField(upload_to='archivos_descargables/', help_text="Sube aquí el PDF, .ex5, o .zip")
    
    # Métricas para tu panel Super Root
    descargas = models.IntegerField(default=0, editable=False) # Se actualizará solo
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.categoria}"