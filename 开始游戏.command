#!/bin/zsh
cd -- "${0:A:h}"
if curl -fsS http://127.0.0.1:5178/app.js 2>/dev/null | /usr/bin/grep -q 'starry-v2'; then
  open http://localhost:5178/
  exit 0
fi
python3 serve.py &
server_pid=$!
trap 'kill "$server_pid" 2>/dev/null' EXIT INT TERM
for i in {1..30}; do
  if curl -fsS http://127.0.0.1:5178/app.js >/dev/null 2>&1; then
    open http://localhost:5178/
    wait "$server_pid"
    exit $?
  fi
  sleep 0.2
done
print '启动失败：请检查 5178 端口是否被其他程序占用。'
wait "$server_pid"
