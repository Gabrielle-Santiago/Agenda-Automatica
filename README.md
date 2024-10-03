# Sistema de Agendamento
## Objetivo
<p> A principal funcionalidade da aplicação é desenvolver uma solução para o gerenciamento e agendamento de serviços, integrando tecnologias como Python e Javascript. O projeto busca automatizar e otimizar o processo de agendamento, garantindo eficiência operacional, escalabilidade e uma experiência de usuário superior. Além disso, o sistema será capaz de se integrar com dispositivos IoT para informação de quando produtos cadastrados no sistema estiverem a baixo do nível, emitir um aviso via e-mail.</p>

## Organização da arquitetura

### Branchs e suas funcionalidades
#### Main
Onde encontra-se a conclusão do projeto e suas funcionalidades, que foram desenvolvidas em branchs específicas, aprovadas e unidas ao main.

#### FronEnd-Agendamento
Foca na criação e estilização dos templates. Abaixa encontrasse as funções realizadas
- Criação das páginas HTML
- Adição do conteúdo de cada página
- Organização das pastas do projeto
- Conexão com CSS
- Estilização das páginas, acrescentando imagens, logo empresarial, mantendo de forma extensível e afins

#### BackEnd-Agendamento
Tem como intuito a integração do front-end à suas devidas funcionalidades e manter o devido funcionamento das respostas enviadas.
- Desenvolvimento da lógica do cadastro, autenticação e gerenciamento de perfis de usuários
- Verificação do envio dos formulários
- Recebimento e encaminhamento das respostas enviadas através do Front-End
- Organização e criação da lógica por trás da aplicação como o views, forms, models...

#### Cloud-Integration
Visa a integração com o banco de dados
- Banco de dados selecionado foi o MySQL
- Recebimento e armazenamento das informações provinda dos formulários

#### JavaScript
Concentra-se em deixar o layout do usuário dinâmico
- Na página cadastroProduto, cria novas divs para acrescentar novos ingredientes e suas respectivas quantidades
- Captura a interação do usuário com a seleção dos produtos, acrescenta e busca detalhes do mesmo no banco de dados (a página que ocorre é a 'produtosCadastrados.html')

#### Arduino
É dedicado à incorporar os dispositivos iot para a aplicação, utilizando de um simulador de placa de circuíto para utilizar sensores que monitoram as quantidades de produtos e enviam dados para o sistema

#### Email
Desenvolvimento do script do email e a lógica do envio do mesmo para o usuário 24h antecipadas para relembrar do comprimisso agendado

### Pastas

Agenda-Automática/
- `.venv/` (ambiente virtual)
- `AgendaAutomatica/`
  - `AgendaAutomatica/` (contém as configurações do Django, como settings, URLs, etc.)
  - `static/`
    - `css/`
      - `style.css` (estilização das páginas)
    - `js/`
      - `configProduto.js` 
      - `index.js`
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
* Django é um framework para desenvolvimento rápido para web, escrito em Python, que foi aplicado para desenvolvimentos e configurações dos templates e de seus respectivos retornos
* Bootstrap é um framework web com código-fonte aberto para desenvolvimento de componentes de interface, o qual foi aplicado para organização dos formulários, na lista dos agendamentos marcados e no menu da aplicação

## Visualização
Abaixo encontrasse imagens feitas no Figma que possuem intuito de mostrar como deve ocorrer a visualização das páginas

Aqui mostra a tela com o que o cliente possue o primeiro contato
![Agendamento](https://github.com/user-attachments/assets/675ec8a0-b5ce-4ecc-8833-f14b57339785)

Já nesse é focado no proprietário, onde possa cadastrar ou visualizar a agenda do dia
![AgendamentoDois](https://github.com/user-attachments/assets/9a81807b-2e95-4990-b0bc-e06157cfc959)
