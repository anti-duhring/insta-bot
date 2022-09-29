from scripts.reply_comments import ReplyBot

username = 'username'
password = 'password'
post_link = 'post_id'
comment_text = 'Obrigado pelo comentário!'

ReplyBot().initialize_crawler(post_link=post_link, username=username, password=password, comment_text=comment_text)