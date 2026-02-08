# Sistema de Controle de Estoque de TI (ITAM)

## 1. Visão Geral do Projeto
Desenvolvimento de um sistema web para **Gestão de Ativos de TI (IT Asset Management - ITAM)**. O objetivo é substituir o controle manual/planilhas, permitindo rastreabilidade total de notebooks, periféricos e chips, controlando o ciclo de vida (aquisição, empréstimo, manutenção e descarte).

## 2. Stack Tecnológico

A escolha das tecnologias prioriza performance, tipagem estática (para reduzir bugs) e facilidade de deploy em borda (Edge).

### 2.1 Backend (API)
* **Linguagem:** Python 3.12+
* **Framework:** **FastAPI** (Alta performance, documentação automática via Swagger UI).
* **ORM:** **SQLAlchemy (Async)** (Padrão ouro para ORM em Python).
* **Validação de Dados:** **Pydantic v2**.
* **Autenticação:** OAuth2 com JWT (JSON Web Tokens) e Hashing de senhas com `bcrypt`.
* **Testes:** Pytest.

### 2.2 Banco de Dados
* **Database:** **Turso** (baseado em SQLite/LibSQL).
* **Driver:** `aiosqlite` ou driver nativo do LibSQL compatível com SQLAlchemy.
* **Gerenciamento de Migrações:** **Alembic**.

### 2.3 Frontend (SPA)
* **Framework:** **React** (com TypeScript).
* **Build Tool:** Vite.
* **Estilização:** **Tailwind CSS** (Produtividade e padrão moderno).
* **Componentes UI:** **Shadcn/UI** (Componentes acessíveis e customizáveis) ou Radix UI.
* **Gerenciamento de Estado/Server State:** **TanStack Query (React Query)** (Para cache e sincronização com a API).
* **Roteamento:** React Router DOM.
* **Ícones:** Lucide React.

## 3. Arquitetura do Banco de Dados (Schema)

O banco de dados deve ser normalizado. Abaixo, a estrutura sugerida das tabelas principais.

### Tabela: `users` (Acesso ao Sistema)
* `id` (PK, UUID ou Integer)
* `username` (String, Unique)
* `password_hash` (String)
* `role` (Enum: `ADMIN`, `COMMON`)
* `active` (Boolean)

### Tabela: `employees` (Pessoas/Setores que recebem itens)
* `id` (PK)
* `name` (String)
* `department` (String - Setor)
* `email` (String, Optional)
* `active` (Boolean - Default True)

### Tabela: `categories` (Tipos de Itens)
* `id` (PK)
* `name` (String - Ex: Notebook, Fonte, Chip)
* `description` (String, Optional)

### Tabela: `items` (O Inventário)
* `id` (PK)
* `category_id` (FK -> categories.id)
* `patrimony_number` (String, Unique, Index)
* `serial_number` (String, Optional, Index)
* `acquisition_date` (Date)
* `status` (Enum: `AVAILABLE`, `IN_USE`, `MAINTENANCE`, `DISCARDED`)
* `notes` (Text)
* `created_at` (Datetime)
* `updated_at` (Datetime)

### Tabela: `movements` (Histórico)
* `id` (PK)
* `item_id` (FK -> items.id)
* `employee_id` (FK -> employees.id, Nullable - Caso seja manutenção ou baixa sem funcionário)
* `user_id` (FK -> users.id - Quem registrou a ação)
* `type` (Enum: `LOAN`, `RETURN`, `MAINTENANCE_SEND`, `MAINTENANCE_RETURN`, `DISCARD`)
* `movement_date` (Datetime)
* `observation` (String - Estado do item na devolução, etc.)

## 4. Endpoints da API (Design RESTful)

### Autenticação
* `POST /auth/token`: Login (retorna Access Token).

### Itens (Items)
* `GET /items`: Listagem com filtros (status, tipo, busca textual).
* `GET /items/{id}`: Detalhes do item + histórico recente.
* `POST /items`: Criar novo item.
* `PUT /items/{id}`: Atualizar dados (não atualiza status diretamente, usar endpoint de movimentação).
* `DELETE /items/{id}`: Soft delete ou bloqueio se houver histórico.

### Pessoas/Setores (Employees)
* `GET /employees`: Listar funcionários.
* `POST /employees`: Cadastrar.
* `PUT /employees/{id}`: Editar.

### Movimentações (Core Business Logic)
* `POST /movements/loan`: Realizar empréstimo.
    * *Payload:* `{item_id, employee_id, date}`.
    * *Validação:* Item deve estar `AVAILABLE`.
* `POST /movements/return`: Realizar devolução.
    * *Payload:* `{item_id, condition_notes, date}`.
    * *Efeito:* Muda status para `AVAILABLE` (ou `MAINTENANCE` se defeituoso).
* `POST /movements/maintenance`: Enviar/Retornar da manutenção.

### Relatórios (Reports)
* `GET /reports/dashboard`: Contagem rápida (Total itens, Itens em uso, Itens disponíveis).
* `GET /reports/loans`: Itens emprestados atualmente.
* `GET /reports/history/{item_id}`: Linha do tempo completa do item.

## 5. Regras de Negócio e Validações

1.  **Imutabilidade do Histórico:** Registros na tabela `movements` nunca devem ser deletados, apenas consultados.
2.  **Exclusividade de Posse:** Um item com status `IN_USE` não pode ser emprestado novamente até que ocorra uma devolução (`RETURN`).
3.  **Integridade de Exclusão:** Um item que possui movimentações não pode ser deletado do banco (`HARD DELETE`). Deve-se alterar seu status para `DISCARDED` (Baixa).
4.  **Permissões:**
    * `COMMON`: Apenas GET (leitura) em todas as rotas.
    * `ADMIN`: Acesso total (GET, POST, PUT, DELETE).

## 6. Configuração e Boas Práticas

### 6.1 Variáveis de Ambiente (.env)
O sistema deve usar `pydantic-settings` para gerenciar:
```env
DATABASE_URL="sqlite+libsql://<SEU_TURSO_TOKEN>@<SEU_TURSO_URL>"
SECRET_KEY="sua_chave_secreta_jwt"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 6.2 Frontend Structure
Organizar o React por funcionalidades (Features) e não apenas por tipos de arquivo:
```text
src/
  features/
    inventory/       (Componentes, hooks e serviços de Itens)
    movements/       (Telas de empréstimo/devolução)
    auth/            (Login)
  components/
    ui/              (Botões, Inputs, Cards - Shadcn)
  lib/               (Configuração do Axios, Utils)
```

### 6.3 Padrões de Código
* **Backend:** Seguir PEP 8. Usar Type Hints estritos.
* **Frontend:** Usar ESLint + Prettier. Interfaces TypeScript para todas as respostas da API.
* **Tratamento de Erros:** O Backend deve retornar `HTTPException` com detalhes claros (ex: "Item já está emprestado" -> 409 Conflict).

## 7. Passos de Implementação Sugeridos

1.  **Setup Inicial:** Configurar repositório, Poetry (Python) e Vite (React).
2.  **Database:** Criar banco no Turso, configurar SQLAlchemy e rodar primeira migração com as tabelas.
3.  **Auth:** Implementar login e proteção de rotas.
4.  **CRUD Básico:** Implementar cadastro de Itens e Pessoas.
5.  **Lógica de Movimentação:** Criar endpoints de check-in/check-out com validação de status.
6.  **Frontend Integration:** Criar telas consumindo a API.
7.  **Dashboard:** Criar tela inicial com indicadores. 

## Deploy
O deploy será feito no Vercel.