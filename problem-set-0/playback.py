# ler a string
# verificar se há espaços
# caso existam espaços, substituir por "..."

text = "This is CS50"
dots = "..."

new_text = ""
new_text = text.replace(' ', dots)

print(new_text)