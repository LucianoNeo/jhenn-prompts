# Jhenn VEO3 Prompts - Production Site

**🌐 URL oficial:** https://jhenn-prompts.vercel.app

**📦 Repositório:** https://github.com/LucianoNeo/jhenn-prompts

**🚀 Deployment:** Automático via Vercel + GitHub

## Estrutura
- `index.html` — Site principal (cards por dia, prompts, legenda/hashtags)
- `serve.py` — Servidor local para desenvolvimento
- `start-server.bat` — Inicia servidor local

## Desenvolvimento local
```bash
cd prompts-site
python serve.py
# Acesse http://localhost:8080
```

## Deploy
- Auto-deploy ativado: qualquer push na `main`/`master` → Vercel
- Produção: https://jhenn-prompts.vercel.app

## Adicionar novos prompts
Editar `index.html` na seção `promptsByDay`:
```javascript
"2026-03-24": [
  {
    id: 'musica_nova_1',
    title: 'Nova Musica - Prompt 1',
    tags: ['Banda', 'Musica'],
    preview: 'Preview curto...',
    content: `Prompt completo...`,
    metadata: {
      postTitle: "Musica - Artista (piano cover) #jhenn",
      hashtags: "#jhenn #artista #musica #piano #metal #fyp"
    }
  }
]
```
