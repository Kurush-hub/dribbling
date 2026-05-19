const api = localStorage.getItem('api') || 'http://localhost:8000';
const list = document.getElementById('list');

function skeleton() {
  list.innerHTML = '<div class="skeleton"></div><div class="skeleton"></div>';
}

function card(m) {
  const free = m.players_limit - m.players_count;
  return `<article class="card"><h3>${m.title}</h3><p>${m.city} • ${new Date(m.match_date).toLocaleString()}</p><p>${m.game_format} • ${m.location}</p><p>Свободно мест: ${free}</p><button onclick="join('${m.match_id}')">Присоединиться</button></article>`;
}

async function load() {
  skeleton();
  const city = document.getElementById('city').value;
  try {
    const res = await fetch(`${api}/all?city=${encodeURIComponent(city)}`);
    const data = await res.json();
    list.innerHTML = data.map(card).join('') || '<p>Матчи не найдены.</p>';
  } catch {
    list.innerHTML = '<p>Не удалось загрузить матчи.</p>';
  }
}

async function join(id) {
  await fetch(`${api}/join`, { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({match_id:id}) });
  load();
}

window.join = join;
document.getElementById('loadBtn').onclick = load;
document.getElementById('createBtn').onclick = async () => {
  const payload = {title:'Вечерний матч',city:document.getElementById('city').value,location:'Стадион Центральный',match_date:new Date(Date.now()+86400000).toISOString(),game_format:'5x5',players_limit:10,price:20,comment:'MVP demo'};
  await fetch(`${api}/create`, {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)});
  load();
};
load();
