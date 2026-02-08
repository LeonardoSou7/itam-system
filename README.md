# 🖥️ ITAM System - Sistema de Controle de Estoque de Equipamentos de Informática

Sistema completo de gerenciamento de ativos de TI (IT Asset Management) com backend em Python/FastAPI e frontend moderno.

## 📋 Funcionalidades

- **Gestão de Equipamentos**: Controle completo de inventário de equipamentos de informática
- **Gestão de Funcionários**: Cadastro e gerenciamento de colaboradores
- **Autenticação e Autorização**: Sistema seguro com JWT tokens
- **API RESTful**: Backend com FastAPI
- **Interface Moderna**: Frontend responsivo e intuitivo

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.x**
- **FastAPI**: Framework web moderno e rápido
- **SQLAlchemy**: ORM para banco de dados
- **Alembic**: Migrations de banco de dados
- **JWT**: Autenticação com tokens
- **SQLite/PostgreSQL**: Banco de dados

### Frontend
- **React/Next.js**: Framework frontend
- **TypeScript**: Tipagem estática
- **TailwindCSS**: Framework CSS

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- Node.js 16+
- npm ou yarn

### Backend

```bash
# Navegar para o diretório backend
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows)
.\venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Executar migrações
alembic upgrade head

# Iniciar servidor
uvicorn app.main:app --reload
```

O backend estará disponível em `http://localhost:8000`
Documentação da API: `http://localhost:8000/docs`

### Frontend

```bash
# Navegar para o diretório frontend
cd frontend

# Instalar dependências
npm install

# Iniciar servidor de desenvolvimento
npm run dev
```

O frontend estará disponível em `http://localhost:3000`

## 📁 Estrutura do Projeto

```
.
├── backend/          # API e lógica de negócio
│   ├── app/         # Código da aplicação
│   │   ├── api/     # Endpoints da API
│   │   ├── models/  # Modelos do banco de dados
│   │   ├── schemas/ # Schemas Pydantic
│   │   └── core/    # Configurações e utilidades
│   └── alembic/     # Migrations do banco de dados
├── frontend/        # Interface do usuário
│   ├── src/         # Código fonte
│   └── public/      # Arquivos estáticos
├── PRD.md           # Product Requirements Document
└── SPECS.md         # Especificações técnicas

```

## 📝 Documentação

- [PRD.md](./PRD.md) - Requisitos do produto
- [SPECS.md](./SPECS.md) - Especificações técnicas detalhadas

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` no diretório backend com:

```env
DATABASE_URL=sqlite:///./itam.db
SECRET_KEY=sua-chave-secreta-aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto está sob a licença MIT.

## 👨‍💻 Autor

Desenvolvido por LeonardoSou7

---

**Status do Projeto:** 🚧 Em Desenvolvimento
