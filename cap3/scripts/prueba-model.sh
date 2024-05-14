curl -w "\n" -X 'POST' \
'http://127.0.0.1:8000/todo' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"id": 5, "item": "Validation models help with input types"}'
