🧪 Desafios de Playwright (QA Automation)
🟢 Nível 1 — Base sólida
1. Verificar se o site abriu corretamente

👉 Site: https://alesc.sc.gov.br

Tarefa:

abrir o site
validar o título da página

💡 Dica:

expect(page).to_have_title(...)
2. Validar botão visível
validar que o botão “Serviços” existe e está visível

💡 Dica:

page.get_by_role(...)
expect(...).to_be_visible()
3. Clicar em menu e validar mudança
clicar em “Serviços”
validar que algo novo apareceu na tela
🟡 Nível 2 — Interação real
4. Navegação entre páginas
clicar em “Serviços”
clicar em “Intranet”
validar que navegou ou abriu popup
5. Trabalhar com popup (ESSENCIAL)
clicar em link que abre nova aba
capturar essa aba com expect_popup
validar URL ou título
6. Validar texto na tela
depois de abrir qualquer página
verificar se existe um texto específico

💡 Ex:

expect(page.get_by_text("Intranet")).to_be_visible()
🔴 Nível 3 — QA real
7. Teste de regressão simples
abrir site
clicar em menus principais
garantir que nenhum dá erro
8. Teste de link quebrado
pegar 5 links da página
validar se todos respondem (status 200)
9. Teste com espera inteligente
clicar em algo que demora pra carregar
usar wait_for_selector
🧠 Nível 10x (quando estiver confortável)
10. Criar mini “framework”
separar código em funções:
abrir site
clicar menu
validar página
💡 Regra de ouro (pra você evoluir rápido)

👉 1 desafio por vez
👉 se travar: documentação primeiro
👉 depois pergunta aqui com o erro específico