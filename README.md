# TechFlow Solutions

Este projeto consiste em um sistema de gerenciamento de tarefas desenvolvido para a startup de logística fictícia **TechFlow Solutions**[cite: 1].

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.10[cite: 1]
- **Framework de Testes:** Pytest[cite: 1]
- **Integração Contínua:** GitHub Actions[cite: 1]

## 📋 Justificativa da Mudança de Escopo
Durante o primeiro ciclo de desenvolvimento, identificou-se a necessidade crítica de acompanhar o fluxo de trabalho permitindo ao usuário marcar tarefas como **Concluídas**[cite: 1].
- **Impacto no Kanban:** O card de alteração de escopo foi adicionado e priorizado[cite: 1].
- **Impacto no Código:** Criado o método `complete_task` no gerenciador, totalmente coberto por testes automatizados[cite: 1].

## 🚀 Como Executar o Projeto Localmente

1. Instalar as dependências:
   ```bash
   pip install -r requirements.txt