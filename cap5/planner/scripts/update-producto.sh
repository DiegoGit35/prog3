curl -X 'PUT' \
  "http://localhost:8000/productos/$1" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d "{
  "categoria": $2,
  "descripcion": $3,
  "nombre": $4,
  "precio": $5,
  "stock": $6,
  "stock_maximo": $7,
  "stock_minimo": $8
}"

