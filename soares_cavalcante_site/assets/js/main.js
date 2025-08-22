
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
  const body=encodeURIComponent(lines.join('

'));
  if(msg){msg.classList.remove('hidden');setTimeout(()=>msg.classList.add('hidden'),4000)}
  location.href=`mailto:atendimento@soaresecavalcante.com?subject=${subject}&body=${body}`;
  return false;
}
