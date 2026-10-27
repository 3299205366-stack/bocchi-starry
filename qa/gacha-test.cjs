const fs=require('fs'),vm=require('vm'),assert=require('assert');const src=fs.readFileSync(__dirname+'/../dist/gacha.js','utf8');const ctx={state:{},$(){return{}},$$(){return[]}};vm.createContext(ctx);vm.runInContext(src.slice(0,src.indexOf('function cardHTML'))+';this.draw=drawCards;this.pool=CARD_POOL;',ctx);
let g={pity:0,total:0,cards:{}};let a=ctx.draw(g,10,()=>.9);assert(a.some(c=>c.rarity==='SR'));assert.equal(new Set(a.map(c=>c.id)).size,10);assert.equal(g.total,10);assert.equal(g.pity,10);
a=ctx.draw(g,10,()=>.9);a=ctx.draw(g,10,()=>.9);assert.equal(a[9].rarity,'SSR');assert.equal(g.pity,0);assert.equal(Object.values(g.cards).reduce((a,b)=>a+b,0),30);
g={pity:29,total:29,cards:{}};assert.equal(ctx.draw(g,1,()=>.9)[0].rarity,'SSR');assert.equal(g.pity,0);
g={pity:0,total:0,cards:{}};assert.equal(ctx.draw(g,1,()=>0)[0].rarity,'SSR');assert.equal(ctx.draw(g,1,()=>0)[0].isNew,false);
for(let j=0;j<1000;j++){a=ctx.draw(g,10);assert(a.some(c=>c.rarity!=='R'));assert.equal(new Set(a.map(c=>c.id)).size,10);assert(g.pity<30)}
for(const c of ctx.pool)assert(fs.existsSync(__dirname+'/../dist/'+c.img));console.log('PASS: ten-pull guarantee, shared pity/reset, duplicates, 1000 batches, all card assets');
