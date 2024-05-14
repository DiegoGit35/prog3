curl -w "\n" -X 'POST' \
'http://127.0.0.1:8000/productos' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ 
    "id": 1,
    "nombre":"Mesa", 
    "categoria": "Mueble", 
    "descripcion": "Una mesa de comedor", 
    "precio": 120000.00,
    "stock": 10, 
    "stock_minimo": 5, 
    "stock_maximo": 25, 
    "activo": true 
}'