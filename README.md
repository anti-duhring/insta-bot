# Insta-Bot :robot: :camera_flash:
O Insta-Bot serve para, de forma automática, responder todos os comentários principais de um post (ou seja, comentários que não estão dentro de comentários).

## Configuração
A configuração é bem simples e deve ser feita diretamente no arquivo `main.py`
```python
from scripts.reply_comments import ReplyBot

username = 'username'
password = 'password'
post_link = 'post_id'
comment_text = 'Obrigado pelo comentário!'

ReplyBot().initialize_crawler(post_link=post_link, username=username, password=password, comment_text=comment_text)
```

- `username`: Nome do usuário sem o arroba (@).
- `password`: Senha da conta.
- `comment_text`: Texto que será respondido.
- `post_link`: O ID do link da foto. Por exemplo, no caso dessa foto: `https://www.instagram.com/p/CfewtyLJBGU/` o `post_link` será `CfewtyLJBGU`.

## Tecnologias
- Selenium
- Chromedriver

## Contribuição
Sinta-se livre pra contribuir, seja melhorando o script ou adicionando outras funcionalidades. 