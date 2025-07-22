#!/bin/sh
echo "🚀 [start.sh] Arrancando aplicación en $(date)"
uvicorn main:app --host 0.0.0.0 --port 8000 --log-level debug
