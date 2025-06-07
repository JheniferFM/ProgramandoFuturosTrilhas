-----

# Plataforma de Trilhas de Estudo em TI: Conectando Conhecimento e Voluntariado

Bem-vindo à **Plataforma de Trilhas de Estudo em TI**, um projeto colaborativo que visa democratizar o acesso a conteúdo de qualidade em diversas áreas da Tecnologia da Informação. Aqui, entusiastas e profissionais de TI podem encontrar **trilhas de estudo estruturadas** e **voluntários com experiência** podem contribuir ativamente para o desenvolvimento e aprimoramento dessas trilhas, criando um ambiente dinâmico de aprendizado contínuo.

-----

## 🚀 Funcionalidades Principais

Esta aplicação mínima viável (MVP) oferece as seguintes funcionalidades:

  * **Exploração de Trilhas:** Visualize uma lista de trilhas de estudo disponíveis com títulos, descrições e níveis de dificuldade.
  * **Detalhes da Trilha:** Acesse uma trilha específica para ver seus módulos e conteúdos.
  * **Autenticação de Usuários:**
      * **Registro:** Crie contas como "Aprendiz" ou "Voluntário".
      * **Login/Logout:** Gerencie sessões de usuário.
  * **Criação de Conteúdo (para Voluntários):**
      * **Criar Nova Trilha:** Voluntários logados podem propor e criar novas trilhas de estudo.
      * **Adicionar Módulos:** Inclua módulos e seus respectivos conteúdos em trilhas existentes.

-----

## 💻 Tecnologias Utilizadas

Este projeto foi desenvolvido com as seguintes tecnologias:

  * **Backend:**
      * **Python 3:** Linguagem de programação principal.
      * **Flask:** Micro-framework web para o desenvolvimento do servidor.
      * **SQLite3:** Banco de dados leve e integrado, ideal para prototipagem e pequenos projetos.
  * **Frontend:**
      * **HTML5:** Estrutura das páginas web.
      * **CSS3:** Estilização e design da interface do usuário.
      * **JavaScript:** (Ainda não amplamente utilizado neste MVP, mas presente para futuras interações).
  * **Arquitetura:**
      * **MVC (Model-View-Controller):** Padrão de design para organização do código.

-----

## ⚙️ Como Configurar e Rodar o Projeto

Siga estes passos para ter a aplicação rodando em sua máquina local.

### Pré-requisitos

Certifique-se de ter o **Python 3** instalado em seu sistema.

### 1\. Clonar o Repositório (ou Criar a Estrutura)

#### Opção A: Se você já tem o código em pastas

Se você já criou a estrutura de pastas e arquivos manualmente, apenas navegue até a pasta `plataforma_trilhas` no seu terminal.

```bash
cd plataforma_trilhas
```

#### Opção B: Se você está começando do zero (recomendado para GitHub)

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd plataforma_trilhas
```

### 2\. Instalar as Dependências

Dentro da pasta `plataforma_trilhas`, instale o Flask usando pip:

```bash
pip install Flask
```

Você pode ver um aviso para atualizar o `pip`. Siga a sugestão se desejar:

```bash
python -m pip install --upgrade pip
```

### 3\. Inicializar o Banco de Dados

É crucial que o banco de dados e suas tabelas sejam criados antes de rodar a aplicação.

1.  **Gere o arquivo `schema.sql`:** Este arquivo está na raiz do seu projeto.

2.  **Execute o script de inicialização do DB:**

    ```bash
    python database.py
    ```

    Você deverá ver a mensagem: `Banco de dados inicializado.`

    *Se você já tentou rodar antes e teve erros como "no such table", é recomendável parar o servidor Flask (se estiver rodando com `CTRL+C`), excluir o arquivo `database.db` (se existir) na raiz do projeto e então executar `python database.py` novamente.*

### 4\. Rodar a Aplicação

Com as dependências instaladas e o banco de dados inicializado, você pode iniciar o servidor Flask:

```bash
python app.py
```

Você verá mensagens como:
`* Serving Flask app 'app'`
`* Debug mode: on`
`* Running on http://127.0.0.1:5000`

### 5\. Acessar no Navegador

Abra seu navegador e vá para o endereço:
[http://127.0.0.1:5000/](https://www.google.com/search?q=http://127.0.0.1:5000/)

-----

## 🔑 Acessando a Plataforma

  * **Usuários de Teste (já inseridos via `schema.sql`):**
      * **Voluntário:**
          * Usuário: `voluntario1`
          * Senha: `senha123`
      * **Aprendiz:**
          * Usuário: `aprendiz1`
          * Senha: `senha456`
  * Você também pode registrar novos usuários pela página de `Registrar`.

-----

## 🤝 Como Contribuir

Sua ajuda é muito bem-vinda para expandir esta plataforma\!

1.  **Faça um Fork** do repositório.
2.  **Crie uma Branch** para sua feature (`git checkout -b feature/minha-nova-funcionalidade`).
3.  **Faça suas Alterações** e teste-as.
4.  **Faça Commit** de suas mudanças (`git commit -m 'feat: adiciona nova funcionalidade X'`).
5.  **Faça Push** para a branch (`git push origin feature/minha-nova-funcionalidade`).
6.  **Abra um Pull Request** detalhando suas alterações.

-----

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](https://www.google.com/search?q=LICENSE) para mais detalhes.

-----

## 📞 Contato

Em caso de dúvidas, sinta-se à vontade para abrir uma issue no repositório do GitHub.

-----

Este README está bem completo e deve ajudar qualquer pessoa a entender e rodar seu projeto. Lembre-se de criar o arquivo `LICENSE` na raiz do seu projeto (geralmente um arquivo de texto simples com o conteúdo da licença MIT).
