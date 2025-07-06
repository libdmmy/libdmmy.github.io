dev:
    uv run mkdocs serve

push:
    git add .
    git commit -m "update from $(date)"
    git push
