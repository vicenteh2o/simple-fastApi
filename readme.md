# curl request

curl -X POST -H "Content-Type: application/json" -d '{"text":"apple"}' 'http://127.0.0.1:8000/items'
curl -X GET 'http://127.0.0.1:8000/items?limit=3'
