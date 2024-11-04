# Sistema de Agenda Automática
## Objetivo
<p> A aplicação Agenda Automática visa gerenciar e otimizar o agendamento de serviços, integrando tecnologias como Python, Django, e JavaScript para uma experiência de usuário eficiente e automatizada. O sistema permite aos clientes agendarem compromissos e envia automaticamente um e-mail de lembrete 24 horas antes do compromisso. As datas passadas são removidas automaticamente, mantendo uma agenda organizada. O proprietário também pode bloquear dias ou horários específicos sem necessidade de conhecimento técnico e adicionar ou remover clientes manualmente conforme necessário, reduzindo notificações desnecessárias aos clientes e facilitando a administraçãoA principal funcionalidade da aplicação é desenvolver uma solução para o gerenciamento e agendamento de serviços, integrando tecnologias como Python e Javascript. O projeto busca automatizar e otimizar o processo de agendamento, garantindo eficiência operacional, escalabilidade e uma experiência de usuário superior. Além disso, o sistema será capaz de emitir um aviso via e-mail para os clientes agendados 24h antecipadamente para relembra-lo do compromisso marcado, e após o dia acabar as datas passadas serão retiradas automaticamente da agenda, mantendo uma organização viável para o usuário. E em casos do usuário necessitar retirar um dia útil da agenda, haverá uma tela para remover dias e horários necessários ou em casos que precisam da adição/remoção de um cliente manualmente. Acarretando na diminuição da quantidade de avisos que seriam feitos para informar aos clientes. </p>

## Organização da arquitetura

### Branchs e suas funcionalidades
#### Main
Onde encontra-se a conclusão do projeto e suas funcionalidades, que foram desenvolvidas em branchs específicas, aprovadas e unidas ao main.

#### FronEnd-Agendamento
Focado na criação e estilização dos templates, incluindo:
- Criação das páginas HTML e organização do conteúdo
- Estruturação e organização das pastas do projeto
- Conexão e integração com CSS para estilização
- Design extensível e inclusão de logotipos e outros elementos visuais

#### BackEnd-Agendamento
Responsável por integrar o front-end às funcionalidades, assegurando que as respostas e os dados enviados sejam processados corretamente:
- Desenvolvimento da lógica do cadastro, autenticação e gerenciamento de horários
- Verificação do envio dos formulários e recebimento pelo banco de dados
- Controle das views, models, forms e configuração de URLs

#### Cloud-Integration
Visa a integração com o banco de dados
- Integração com o PostgreSQL para armazenamento seguro e escalável
- Configuração de segurança e backups periódicos dos dados

#### JavaScript
Concentra-se em deixar o layout do usuário dinâmico
- Na página de "Agendados", oculta e acrescenta informações sobre os clientes de forma interativa

#### Email
Responsável pelo desenvolvimento do sistema de notificação:
- Lógica de envio de e-mails automatizados 24 horas antes do compromisso, alertando os clientes

### Pastas

Agenda-Automática/
- `.venv/` (ambiente virtual)
- `AgendaAutomatica/`
  - `AgendaAutomatica/` (contém as configurações do Django, como settings, URLs, etc.)
  - `static/`
    - `css/` (estilização das páginas)
      - `auth.css` (referente as páginas dentro de auth, os outros seguem a mesma lógica)
      - `cadastros.css`
      - `icon.css`
      - `main.css`
      - `styles.css` (estilizações gerais, como a fonte, o tamanho das letras e afins)
    - `img/`
      - `icon/`
        - Ícones como sinal de mais e menos
      - `logo/`
        - Contém a logo da empresa
      - `out/`
        - Imagens utilizadas ao fundo para design atrativo
    - `js/`
      - `agendados.js`
- `task/`
  - `migrations/`
    - informações específicas salvas do banco de dados, como pro exemplo: cadastro do Produto, agendamento do horário...
  - `templates/`
    - `auth/`
      - `pedidoPerfume.html`
      - `produtosCadastrados.html`  
    - `cadastros/`
      - `cadastrados.html`
      - `cadastro.html`
      - `cadastroProduto.html`
      - `indisponivel.html`
    - `main/`
      -  `esqueciSenha.html`
      -  `login.html`
    - `menu.html`
  - `Configurações do Django`
  - `_init_.py`
  - `admin.py`
  - `apps.py`
  - `forms.py`
  - `models.py`
  - `views.py`
- `manage.py` (utilizado para iniciar a aplicação do Django)
- `LICENSE`
- `README.md`
- `requirements.txt` (contém as instalações que foram utilizadas)

## Frameworks e Bibliotecas
***Django***
Framework principal para a criação das funcionalidades do sistema, incluindo a gestão de templates, controle de autenticação, e processamento de agendamentos.

***Bootstrap*** 
Utilizado para o desenvolvimento responsivo dos formulários, organização dos agendamentos e elementos no menu, facilitando a navegação tanto no desktop quanto em dispositivos móveis.

## Visualização
Aqui estão algumas imagens criadas no Figma, ilustrando o design esperado para as páginas principais do sistema:

Tela Inicial do Cliente: Primeira interface de contato, com opções de agendamento e visualização de compromissos.
Tela do Proprietário: Interface de administração, onde é possível gerenciar a agenda e realizar cadastros de novos clientes ou compromissos.

## Requisitos de Sistema
<p> Python 3.8+ <br>
PostgreSQL (configurar base de dados com credenciais seguras) <br>
Bootstrap (integrado via CDN no HTML) <br>
</p>

## Guia do Usuário
1. Agendamento pelo Cliente: O cliente acessa a tela inicial, seleciona o dia,horário e procedimento desejado e preenche os dados de contato.
2. Notificação de E-mail: 24 horas antes do compromisso, um e-mail de lembrete é enviado automaticamente ao cliente.
3. Gestão de Dias e Horários pelo Proprietário: O proprietário pode acessar a tela de gerenciamento e desativar dias ou horários para agendamento, além de adicionar novos compromissos manualmente quando necessário.

## Suporte e Contribuição
### Reportar Problemas
Para reportar problemas, abrir uma issue no GitHub detalhando o erro, contexto e possíveis passos para replicar o problema.

### Contato para Suporte
Disponibilizamos um canal de comunicação por e-mail (gabriellesantisilva@gmail.com) para questões técnicas e suporte ao usuário.
