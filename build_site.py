import os, textwrap, zipfile

BASE = "/workspace/soares_cavalcante_site"
ASSETS_CSS = os.path.join(BASE, "assets", "css")
ASSETS_JS  = os.path.join(BASE, "assets", "js")
SERVICOS   = os.path.join(BASE, "servicos")
os.makedirs(ASSETS_CSS, exist_ok=True)
os.makedirs(ASSETS_JS, exist_ok=True)
os.makedirs(SERVICOS, exist_ok=True)


def head(title: str, desc: str, prefix: str = "") -> str:
    return textwrap.dedent(f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>{title} - Soares & Cavalcante</title>
      <meta name="description" content="{desc}">
      <link rel="icon" href="{prefix}assets/favicon.ico">
      <script src="https://cdn.tailwindcss.com"></script>
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
      <link rel="stylesheet" href="{prefix}assets/css/style.css">
      <style>body{{font-family:'Inter',sans-serif}}</style>
    </head>
    <body class="text-gray-800 bg-white">
      <a href="#conteudo" class="sr-only focus:not-sr-only focus:absolute focus:top-2 focus:left-2 focus:bg-white focus:p-2 focus:rounded-md">Pular para conteúdo</a>
      <header class="sticky top-0 z-40 bg-white/90 backdrop-blur border-b">
        <div class="max-w-7xl mx-auto p-4 flex items-center justify-between">
          <a href="{prefix}index.html" class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-xl bg-blue-900 grid place-items-center text-white text-sm font-bold">S&C</div>
            <span class="text-xl font-extrabold text-blue-900">Soares & Cavalcante</span>
          </a>
          <button id="menuBtn" class="md:hidden inline-flex items-center px-3 py-2 border rounded-lg">Menu</button>
          <nav id="nav" class="hidden md:flex items-center gap-6 absolute md:static top-full left-0 w-full md:w-auto bg-white border-b md:border-0 p-4 md:p-0">
            <a class="navlink block py-2 px-3 rounded-lg" href="{prefix}index.html">Início</a>
            <a class="navlink block py-2 px-3 rounded-lg" href="{prefix}servicos.html">Serviços</a>
            <a class="navlink block py-2 px-3 rounded-lg" href="{prefix}sobre.html">Sobre</a>
            <a class="navlink block py-2 px-3 rounded-lg" href="{prefix}contato.html">Contato</a>
          </nav>
        </div>
      </header>
      <main id="conteudo" tabindex="-1">
    """)


def footer(prefix: str = "") -> str:
    return textwrap.dedent(f"""
      </main>
      <footer class="mt-16 border-t bg-gray-50">
        <div class="max-w-7xl mx-auto p-6 grid md:grid-cols-3 gap-8 text-sm">
          <div>
            <div class="flex items-center gap-3 mb-3">
              <div class="w-8 h-8 rounded-lg bg-blue-900 grid place-items-center text-white text-xs font-bold">S&C</div>
              <span class="font-bold text-blue-900">Soares & Cavalcante</span>
            </div>
            <p class="text-gray-600">Excelência em gestão de serviços, segurança e facilities.</p>
          </div>
          <div>
            <h4 class="font-semibold mb-3 text-gray-900">Links</h4>
            <ul class="space-y-2">
              <li><a href="{prefix}servicos.html" class="text-gray-600 hover:underline">Serviços</a></li>
              <li><a href="{prefix}sobre.html" class="text-gray-600 hover:underline">Sobre</a></li>
              <li><a href="{prefix}contato.html" class="text-gray-600 hover:underline">Contato</a></li>
            </ul>
          </div>
          <div>
            <h4 class="font-semibold mb-3 text-gray-900">Contato</h4>
            <p class="text-gray-600">São Paulo - SP<br> atendimento@soaresecavalcante.com<br> (11) 99999-9999</p>
          </div>
        </div>
        <div class="border-t py-4 text-center text-xs text-gray-500">© 2025 Soares & Cavalcante</div>
      </footer>
      <script src="{prefix}assets/js/main.js"></script>
    </body>
    </html>
    """)

# Bodies (compact)
INDEX = textwrap.dedent("""
  <section class="max-w-7xl mx-auto px-6 py-16 grid md:grid-cols-2 gap-10 items-center">
    <div>
      <h1 class="text-4xl md:text-6xl font-extrabold text-blue-900">Soluções em gestão e segurança.</h1>
      <p class="mt-6 text-lg text-gray-700">Performance, redução de custos e experiência superior.</p>
      <div class="mt-8 flex flex-wrap gap-3">
        <a href="contato.html" class="px-6 py-3 rounded-xl bg-blue-900 text-white font-semibold">Solicitar proposta</a>
        <a href="servicos.html" class="px-6 py-3 rounded-xl border border-blue-900 text-blue-900 font-semibold">Ver serviços</a>
      </div>
    </div>
    <div class="aspect-[4/3] rounded-3xl border bg-white shadow-2xl grid place-items-center text-6xl">🏢🔒⚙️</div>
  </section>
  <section class="py-16 bg-gray-50">
    <div class="max-w-7xl mx-auto px-6 grid md:grid-cols-3 gap-6">
      <a href="servicos/portaria-seguranca.html" class="card">🛡️ Portaria & Segurança</a>
      <a href="servicos/mensageria-condominios.html" class="card">📦 Mensageria</a>
      <a href="servicos/facilities-limpeza.html" class="card">🧹 Facilities & Limpeza</a>
    </div>
  </section>
""")

SOBRE = textwrap.dedent("""
  <section class="max-w-7xl mx-auto px-6 py-16">
    <h1 class="text-3xl md:text-4xl font-extrabold text-blue-900 mb-6">Sobre</h1>
    <p class="text-lg text-gray-700">Desde 2020, soluções integradas em segurança, mensageria e facilities.</p>
  </section>
""")

CONTATO = textwrap.dedent("""
  <section class="max-w-3xl mx-auto px-6 py-16">
    <h1 class="text-3xl md:text-4xl font-extrabold text-blue-900 mb-6">Fale conosco</h1>
    <form class="bg-white p-8 rounded-2xl border shadow-lg" onsubmit="return handleFormSubmit(event)">
      <div class="grid gap-6">
        <input required id="nome" name="nome" class="input" placeholder="Nome *">
        <input required type="email" id="email" name="email" class="input" placeholder="E-mail *">
        <input id="telefone" name="telefone" class="input" placeholder="Telefone/WhatsApp">
        <textarea required id="mensagem" name="mensagem" rows="5" class="input" placeholder="Mensagem *"></textarea>
        <div class="flex items-center gap-4">
          <button type="submit" class="px-8 py-3 rounded-xl bg-blue-900 text-white font-semibold">Enviar</button>
          <a class="px-6 py-3 rounded-xl border border-green-500 text-green-600" href="https://wa.me/5511999999999" target="_blank">WhatsApp</a>
        </div>
        <div id="formMsg" class="hidden p-4 bg-green-50 border border-green-200 rounded-lg text-sm">Mensagem preparada! Seu e-mail abrirá.</div>
      </div>
    </form>
  </section>
""")

SERVICOS_PAGE = textwrap.dedent("""
  <section class="max-w-7xl mx-auto px-6 py-16">
    <h1 class="text-3xl md:text-4xl font-extrabold text-blue-900 mb-8">Nossos serviços</h1>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 text-blue-900">
      <a href="servicos/portaria-seguranca.html" class="card">🛡️ Portaria & Segurança</a>
      <a href="servicos/mensageria-condominios.html" class="card">📦 Mensageria</a>
      <a href="servicos/facilities-limpeza.html" class="card">🧹 Facilities & Limpeza</a>
    </div>
  </section>
""")

COMPLIANCE = textwrap.dedent("""
  <section class="max-w-4xl mx-auto px-6 py-16">
    <h1 class="text-3xl md:text-4xl font-extrabold text-blue-900 mb-4">LGPD & Compliance</h1>
    <p class="text-gray-700">Dados coletados são usados apenas para contato comercial. Solicite exclusão a qualquer momento.</p>
  </section>
""")

NOT_FOUND = textwrap.dedent("""
  <section class="min-h-[60vh] grid place-items-center text-center p-6">
    <div>
      <div class="text-6xl mb-4">🔎</div>
      <h1 class="text-3xl md:text-4xl font-extrabold text-blue-900 mb-3">Página não encontrada</h1>
      <a href="index.html" class="px-6 py-3 rounded-xl bg-blue-900 text-white font-semibold">Voltar</a>
    </div>
  </section>
""")


def service_page(title: str, intro: str, bullets: list[str], icon: str) -> str:
    items = "\n".join([f"<li class='flex items-start gap-2'><span class='text-blue-600 mt-1'>✓</span> {b}</li>" for b in bullets])
    return textwrap.dedent(f"""
      <section class="max-w-5xl mx-auto px-6 py-16">
        <div class="text-center mb-8">
          <div class="text-6xl mb-4">{icon}</div>
          <h1 class="text-3xl md:text-4xl font-extrabold text-blue-900">{title}</h1>
          <p class="mt-4 text-lg text-gray-700">{intro}</p>
        </div>
        <div class="bg-white p-8 rounded-2xl border shadow-lg">
          <h2 class="text-xl font-bold text-blue-900 mb-6">Entregáveis</h2>
          <ul class="space-y-3 text-gray-700">{items}</ul>
        </div>
        <div class="mt-10 flex justify-center gap-4">
          <a href="../contato.html" class="px-8 py-3 rounded-xl bg-blue-900 text-white font-semibold">Solicitar proposta</a>
          <a href="../servicos.html" class="px-6 py-3 rounded-xl border border-blue-900 text-blue-900 font-semibold">Voltar</a>
        </div>
      </section>
    """)

# Write top-level pages
PAGES = {
  "index.html": head("Início", "Soluções inteligentes") + INDEX + footer(),
  "sobre.html": head("Sobre", "Quem somos") + SOBRE + footer(),
  "contato.html": head("Contato", "Fale conosco") + CONTATO + footer(),
  "servicos.html": head("Serviços", "Portfólio") + SERVICOS_PAGE + footer(),
  "compliance.html": head("LGPD & Compliance", "Privacidade") + COMPLIANCE + footer(),
  "404.html": head("Página não encontrada", "Erro 404") + NOT_FOUND + footer(),
}
for name, html in PAGES.items():
    with open(os.path.join(BASE, name), "w", encoding="utf-8") as f:
        f.write(html)

# Service pages (with ../ prefix in head/footer via call below)
services = {
  "portaria-seguranca.html": service_page(
    "Portaria & Segurança",
    "Controle de acesso, monitoramento 24/7 e rondas preventivas.",
    [
      "Cadastro digital e gestão de visitantes",
      "Rondas programadas e registro de ocorrências",
      "Monitoramento CFTV com alarmes",
    ],
    "🛡️",
  ),
  "mensageria-condominios.html": service_page(
    "Mensageria para Condomínios",
    "Gestão de encomendas ponta a ponta com rastreabilidade.",
    [
      "Registro de entrada e saída",
      "Notificações automáticas",
      "Entrega com protocolo digital",
    ],
    "📦",
  ),
  "facilities-limpeza.html": service_page(
    "Facilities & Limpeza",
    "Asseio, conservação e pós-obra.",
    [
      "Rotinas de limpeza personalizadas",
      "Checklists e inspeções",
      "Gestão de insumos e EPIs",
    ],
    "🧹",
  ),
}
for fname, body in services.items():
    with open(os.path.join(SERVICOS, fname), "w", encoding="utf-8") as f:
        f.write(head(fname.replace('.html','').title(), fname, prefix="../") + body + footer(prefix="../"))

# CSS
STYLE = textwrap.dedent("""
:root{--brand:#0b2a6f;--gray-50:#f9fafb}
html{scroll-behavior:smooth}
.card{display:flex;align-items:center;gap:.75rem;padding:1rem;border:1px solid #e5e7eb;border-radius:.75rem;background:#fff;transition:.2s}
.card:hover{transform:translateY(-2px);box-shadow:0 10px 25px -5px rgba(0,0,0,.1)}
.input{width:100%;border:1px solid #e5e7eb;border-radius:.75rem;padding:.75rem 1rem}
.navlink{transition:.2s}
.navlink.active{background:#0b2a6f;color:#fff}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);border:0}
""")
with open(os.path.join(ASSETS_CSS, "style.css"), "w", encoding="utf-8") as f:
    f.write(STYLE)

# JS (menu + active link + form mailto)
JS = textwrap.dedent("""
(function(){
  const btn=document.getElementById('menuBtn');
  const nav=document.getElementById('nav');
  if(btn&&nav){
    btn.addEventListener('click',()=>{
      nav.classList.toggle('hidden');
      btn.setAttribute('aria-expanded', String(!nav.classList.contains('hidden')));
    });
  }
  const current=(location.pathname.split('/').pop()||'index.html');
  document.querySelectorAll('a.navlink').forEach(a=>{const href=(a.getAttribute('href')||'').split('/').pop();if(href===current)a.classList.add('active');});
})();

function handleFormSubmit(e){
  e.preventDefault();
  const form=e.target;const data=new FormData(form);const msg=document.getElementById('formMsg');
  for(const el of form.querySelectorAll('[required]')){if(!String(el.value||'').trim()){alert('Preencha os campos obrigatórios.');return false;}}
  const fields={nome:'Nome',email:'E-mail',telefone:'Telefone',mensagem:'Mensagem'};
  const lines=[];for(const [k,v] of data.entries()){const t=String(v||'').trim();if(t)lines.push(`${fields[k]||k}: ${t}`)}
  const subject=encodeURIComponent('Contato via site - Soares & Cavalcante');
  const body=encodeURIComponent(lines.join('\n\n'));
  if(msg){msg.classList.remove('hidden');setTimeout(()=>msg.classList.add('hidden'),4000)}
  location.href=`mailto:atendimento@soaresecavalcante.com?subject=${subject}&body=${body}`;
  return false;
}
""")
with open(os.path.join(ASSETS_JS, "main.js"), "w", encoding="utf-8") as f:
    f.write(JS)

# Favicon placeholder
with open(os.path.join(BASE, "assets", "favicon.ico"), "wb") as f:
    f.write(b"\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x20\x00\x00\x00\x00\x00\x16\x00\x00\x00")

# Zip (top-level folder included)
ZIP = "/workspace/soares_cavalcante_site_completo.zip"
with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    root = os.path.basename(BASE)
    for r, d, files in os.walk(BASE):
        d[:] = [x for x in d if not x.startswith('.')]
        for name in files:
            full = os.path.join(r, name)
            arc = os.path.join(root, os.path.relpath(full, BASE))
            z.write(full, arcname=arc)

print("OK", BASE, ZIP)