# Documento de Requisitos do Produto (PRD)
## Sistema de Controle de Estoque de Equipamentos de Informática

### 1. Contexto

Atualmente na GFDE CTE da Prefeitura Municipal de Vitória, o controle de notebooks e acessórios (fontes, modems, chips de internet, etc.) é feito de forma manual ou por planilhas. Essa prática dificulta:

*   Saber quantos equipamentos existem disponíveis;
*   Saber a localização exata de cada equipamento;
*   Controlar empréstimos e devoluções de forma eficiente;
*   Identificar equipamentos defeituosos ou extraviados.

Diante disso, solicita-se o desenvolvimento de um sistema de controle de estoque de equipamentos de informática, voltado para uso interno.

### 2. Objetivo do Sistema

Criar um sistema que permita:

*   Cadastrar e controlar equipamentos de informática;
*   Registrar todas as movimentações (empréstimo, devolução, troca);
*   Monitorar a situação de cada item em tempo real (em uso, disponível, em manutenção, descartado);
*   Gerar relatórios básicos para controle e gestão.

### 3. Tipos de Itens Controlados

O sistema deverá permitir o cadastro e gerenciamento de diferentes tipos de itens, incluindo, mas não se limitando a:

*   Notebooks;
*   Fontes/carregadores;
*   Modems USB;
*   Chips de internet;
*   Outros periféricos (mouse, mochila, etc.).

### 4. Funcionalidades Principais

#### 4.1 Cadastro de Itens

O sistema deve possuir funcionalidade para cadastrar novos itens com as seguintes informações:

*   **Tipo do Item**: (notebook, modem, chip, etc.);
*   **Número de Patrimônio**: Identificador único do ativo;
*   **Número de Série**: (quando existir);
*   **Data de Aquisição**: Data em que o item foi adquirido;
*   **Estado do Item**: (em bom estado, defeituoso, em manutenção, descartado);
*   **Observações**: Campo opcional para notas adicionais.

#### 4.2 Cadastro de Pessoas/Setores

O sistema deve permitir o cadastro de:

*   **Funcionários**: Pessoas físicas que podem utilizar os equipamentos.
*   **Setores**: Departamentos ou áreas da organização.

Cada item pode estar vinculado a uma pessoa ou a um setor.

#### 4.3 Controle de Movimentação

O sistema deve registrar histórico completo de movimentações de cada item:

*   **Empréstimo**:
    *   Para quem foi entregue (Pessoa ou Setor);
    *   Data da entrega;
    *   Responsável pela entrega (usuário do sistema).
*   **Devolução**:
    *   Data da devolução;
    *   Estado do item no momento da devolução.
*   **Troca**:
    *   Registro da substituição de um item por outro.
*   **Manutenção**:
    *   Registro de envio de item para manutenção.
*   **Baixa**:
    *   Registro de descarte do item.

#### 4.4 Status do Item

Cada item deve possuir um status atualizado automaticamente conforme as movimentações:

*   **Disponível**: Item no estoque, pronto para uso.
*   **Em uso**: Item emprestado a uma pessoa ou setor.
*   **Em manutenção**: Item enviado para reparo.
*   **Descartado**: Item baixado do inventário.

**Regra Importante**: O sistema deve impedir o empréstimo de itens que não estejam com o status "Disponível".

#### 4.5 Consulta e Busca

O sistema deve oferecer ferramentas de busca avançada:

*   **Critérios de Busca**:
    *   Número de patrimônio;
    *   Número de série;
    *   Nome da pessoa (responsável atual);
    *   Setor (localização atual);
    *   Tipo de item.
*   **Visualização**:
    *   Quem está com o item atualmente;
    *   Desde quando o item está com o responsável;
    *   Histórico completo de movimentações.

#### 4.6 Relatórios

O sistema deve gerar relatórios para auxiliar na gestão:

*   Lista de todos os itens (filtrável por tipo ou status);
*   Lista de itens emprestados atualmente;
*   Histórico de movimentações por período;
*   Relatório de itens por setor.

### 5. Usuários do Sistema

O sistema terá dois níveis de acesso:

*   **Usuário Administrador**:
    *   Pode cadastrar itens;
    *   Pode cadastrar pessoas/setores;
    *   Pode redefinir senhas;
    *   Pode registrar movimentações (empréstimos, devoluções, etc.).
*   **Usuário Comum**:
    *   Pode apenas consultar informações e relatórios (somente leitura).

### 6. Requisitos Técnicos (Sugestão)

*   **Plataforma**: Sistema Web (acessível via navegador);
*   **Autenticação**: Login e senha individuais;
*   **Banco de Dados**: Para armazenamento seguro das informações;
*   **Interface**: Simples, intuitiva e objetiva;
*   **Auditoria**: Registro automático de data e usuário responsável em cada movimentação realizada no sistema.

### 7. Regras de Negócio

1.  **Exclusividade**: Um item só pode estar vinculado a uma pessoa ou setor por vez.
2.  **Rastreabilidade**: Todo empréstimo deve gerar um registro de movimentação.
3.  **Atualização de Status**: Toda devolução deve permitir a atualização do status do item (ex: de "Em uso" para "Disponível" ou "Defeituoso").
4.  **Preservação de Histórico**: Um item não pode ser excluído permanentemente se já possuir histórico de movimentações; deve ser apenas marcado com status "Descartado" (Soft Delete).
