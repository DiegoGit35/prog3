curl -w "\n" -X 'POST' \
'http://127.0.0.1:8000/todo' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ "id": 1, "item": "Example Schema!" }'

curl -w "\n" -X 'PUT' \
'http://127.0.0.1:8000/todo/1' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"item": "Read the next chapter of the book."
}'
