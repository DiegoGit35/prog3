curl -w "\n" -X  'PUT' \
"http://127.0.0.1:8000/productos/$1/desactivar" \
-H 'accept: application/json' 