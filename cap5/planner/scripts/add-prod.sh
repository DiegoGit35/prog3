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

curl -w "\n" -X 'POST' \
'http://127.0.0.1:8000/productos' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ 
    "id": 2,
    "nombre":"Notebook", 
    "categoria": "Electronica", 
    "descripcion": "Notebook oficina Lenovo", 
    "precio": 1000000.00,
    "stock": 10, 
    "stock_minimo": 5, 
    "stock_maximo": 25, 
    "activo": true 
}'

curl -w "\n" -X 'POST' \
'http://127.0.0.1:8000/productos' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ 
    "id": 3,
    "nombre":"Guitarra Criolla", 
    "categoria": "Instrumentos", 
    "descripcion": "Guitarra criolla C. Robles", 
    "precio": 200000.00,
    "stock": 10, 
    "stock_minimo": 3, 
    "stock_maximo": 10, 
    "activo": true 
}'

curl -w "\n" -X 'POST' \
'http://127.0.0.1:8000/productos' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ 
    "id": 4,
    "nombre":"Guitarra Electrica Cort", 
    "categoria": "Instrumentos", 
    "descripcion": "Cort Aero Custom", 
    "precio": 1200000.00,
    "stock": 5, 
    "stock_minimo": 3, 
    "stock_maximo": 10, 
    "activo": true 
}'

curl -w "\n" -X 'POST' \
'http://127.0.0.1:8000/productos' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ 
    "id": 5,
    "nombre":"Auriculares", 
    "categoria": "Electronica", 
    "descripcion": "Auriculares Redragon", 
    "precio": 150000.00,
    "stock": 10, 
    "stock_minimo": 2, 
    "stock_maximo": 25, 
    "activo": true 
}'

curl -w "\n" -X 'POST' \
'http://127.0.0.1:8000/productos' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ 
    "id": 6,
    "nombre":"Samsung S23", 
    "categoria": "Electronica", 
    "descripcion": "Celular Samsung S23", 
    "precio": 1300000.00,
    "stock": 5, 
    "stock_minimo": 3, 
    "stock_maximo": 10, 
    "activo": true 
}'

curl -w "\n" -X 'POST' \
'http://127.0.0.1:8000/productos' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ 
    "id": 7,
    "nombre":"Kindle Paperwrite", 
    "categoria": "Electronica", 
    "descripcion": "Kindle Paperwrite 10gen", 
    "precio": 300000.00,
    "stock": 8, 
    "stock_minimo": 4, 
    "stock_maximo": 15, 
    "activo": true 
}'