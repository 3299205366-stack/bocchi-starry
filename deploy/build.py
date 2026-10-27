from pathlib import Path
import shutil,hashlib,json
root=Path(__file__).resolve().parents[1];src=root/'dist';out=root/'build'
out.mkdir(exist_ok=True)
# Explicit public artifact set: no development server, venv, backups, references or credentials.
for name in ['index.html','favicon.svg','style.css','theme.css','stories.js','app.js','gacha.js','lyrics.js','listening.js','CREDITS.md']:
 shutil.copy2(src/name,out/name)
for folder in ['musics','albums','fonts']:
 shutil.copytree(src/'assets'/folder,out/'assets'/folder,dirs_exist_ok=True)
art=out/'assets/art';art.mkdir(parents=True,exist_ok=True)
for p in (src/'assets/art').iterdir():
 if p.is_file() and (p.name.startswith(('bocchi-','b-ep','b-yt','大头_'))):shutil.copy2(p,art/p.name)
shutil.copytree(src/'assets/art/official',art/'official',dirs_exist_ok=True)
shutil.copy2(src/'assets/lyrics-sources.json',out/'assets/lyrics-sources.json')
(out/'robots.txt').write_text('User-agent: *\nDisallow: /starry/\n')
files=[p for p in out.rglob('*') if p.is_file()];print(f'{len(files)} files, {sum(p.stat().st_size for p in files)/1024/1024:.1f} MB')
