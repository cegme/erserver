uv run uvicorn coref_api:app --reload --host 0.0.0.0 --port 65535

 curl -X POST "gpu002.cm.cluster:65535/resolve_coref"      -H "Content-Type: application/json"      -d '{"text": "John said he would help Mary. She was grateful."}'

