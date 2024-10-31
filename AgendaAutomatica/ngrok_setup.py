from pyngrok import ngrok

# Configure o token de autenticação
ngrok.set_auth_token("<2oCaZRffbPy3lyWPpG3IsZ7SpCj_RRPRXD3YT3zwUxL7h34P>")

# Inicie um túnel para a porta 8000
public_url = ngrok.connect(8000)
print("URL Público:", public_url)
