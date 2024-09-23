# Sistema de Agendamento
## Objetivo
<p>Desenvolver uma solução para o gerenciamento e agendamento de serviços, integrando tecnologias como Python e Java. O projeto busca automatizar e otimizar o processo de agendamento, garantindo eficiência operacional, escalabilidade e uma experiência de usuário superior. Além disso, o sistema será capaz de se integrar com dispositivos IoT para check-in automatizado e utilizar Big Data para análises preditivas, proporcionando insights estratégicos e personalização de serviços.</p>

## Organização da arquitetura

### Pastas

Agenda-Automática/
- `.venv/` (ambiente virtual)
- `AgendaAutomatica/`
  - `AgendaAutomatica/` (contém as configurações do Django, como settings, URLs, etc.)
  - `static/`
    - `css/`
      - `style.css` (estilização das páginas)
    - `js/`
      - `index.js`
- `task/`
  - `migrations/` (informações específicas salvas do banco de dados, no contexto as informações do cliente)
    - `__init__.py`
    - `0001_initial.py`
  - `templates/`
    - `cadastrados.html`
    - `cadastro.html`
    - `pedidoPerfume.html`
    - `menu.html`
  - `Configurações do Django`
  - `_init_.py`
  - `admin.py`
  - `apps.py`
  - `forms.py`
  - `models.py`
  - `views.py`
- `db.sqlite3` (banco de dados padrão do Django)
- `manage.py` (utilizado para iniciar a aplicação do Django)
- `LICENSE`
- `README.md`
- `requirements.txt` (contém as instalações que foram utilizadas)

### Branchs
- `main` <br>
Possui as funcionalidades princiapais, após ter sido aprovado o funcionamento das mesmas

- `FronEnd-Agendamento` <br>
Foca na creação e estilização dos templates e aquilo que será visualizado pelo usuário

- `BackEnd-Agendamento`<br>
Tem como intuito a integração do front-end à suas devidas funcionalidades, como o vínculo com banco de dados, verificação do envio dos formulários e organização e criação da lógica por trás da aplicação.

- `BigData` <br>
Contém a lógica para receber diversas informações os quais futuramente serão analisados e utilizados para insights

- `Cloud-Integration` <br>
Visa a integração com a nuvem

- `Backend-Email` <br>
Possui a funcionalidade de enviar um e-mail 24h antes do agendamento relembrando o usuário do compromisso

## Divisão de Responsabilidades
### Python:
* Cadastro e armazenamento das respostas dos formulários
* Implementação das regras de negócio relacionadas ao agendamento
* Preparação da infraestrutura para integração com soluções de Big Data
* Registra um novo agendamento se o horário estiver disponível

### Java:
* Desenvolvimento de serviços para envio de notificações por e-mail
* Desenvolvimento de scripts para envio de notificações e lembretes por e-mail

### JavaScript:
* Formatação dos horários, mantendo com uma distância entre cada um, ex: 10:00, 10:30, 11:20, 13:45...
* Verifica se existe conflitos de horários

## Frameworks e Bibliotecas
* Django é um framework para desenvolvimento rápido para web, escrito em Python, que foi aplicado para desenvolvimentos e configurações dos templates e de seus respectivos retornos
* Bootstrap é um framework web com código-fonte aberto para desenvolvimento de componentes de interface, o qual foi aplicado para organização dos formulários, na lista dos agendamentos marcados e no menu da aplicação

