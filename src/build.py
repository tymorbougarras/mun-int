import re
t=open(__import__("os").path.join(__import__("os").path.dirname(__file__),"template.html")).read()
team=[("Président","President","Tymor Bougarras","Co-fondateur||Co-founder"),("Vice-présidente","Vice-President","Lou Dixneuf","Co-fondatrice||Co-founder"),
("Vice-président","Vice-President","Mathieu Viala",""),("Secrétaire générale","Secretary General","Timothée Truong",""),("Trésorière","Treasurer","Violette Milian",""),
("Responsable communication","Head of Communications","Emrick Rakotomahefason",""),("Événementiel et logistique","Events and Logistics","Marwa Ouaboun","")]
cards=""
photos={"Lou Dixneuf":"lou","Mathieu Viala":"mathieu","Timothée Truong":"timothee","Violette Milian":"violette","Marwa Ouaboun":"marwa"}
for fr,en,name,co in team:
    c=f'<div class="co">{{{{{co}}}}}</div>' if co else ""
    ph=photos.get(name)
    pp=f'<div class="pp has"><img class="pic" src="img/bureau_{ph}.jpg" alt="{name}"></div>' if ph else '<div class="pp"><img src="img/logo_munint_white.png" alt=""><span class="todo">{{Photo à fournir||Photo to come}}</span></div>'
    cards+=f'''<div class="member">{pp}
<span class="role">{{{{{fr}||{en}}}}}</span><h4>{name}</h4>{c}<q><span class="todo">{{{{Citation à fournir||Quote to come}}}}</span></q></div>
'''
t=t.replace("[[TEAM]]",cards)
t=re.sub(r"\{\{(.*?)\|\|(.*?)\}\}",lambda m:f'<span class="fr">{m.group(1)}</span><span class="en">{m.group(2)}</span>',t,flags=re.S)
head,rest=t.split("<body",1); body,script=rest.split("<script>",1)
body=re.sub(r">([^<]*)<",lambda m:">"+m.group(1).replace("'","’")+"<",body)
t=head+"<body"+body+"<script>"+script
assert "{{" not in t
open(__import__("os").path.join(__import__("os").path.dirname(__file__),"..","site","index.html"),"w").write(t); print(len(t))
