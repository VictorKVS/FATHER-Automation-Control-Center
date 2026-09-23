import { useMemo, useState } from "react";
import { demoWorkspace } from "./demoData";
import type { AvatarPresence, DataStatus } from "./types";
import "./styles.css";

const statuses: Record<DataStatus,string>={REAL:"REAL",DEMO:"DEMO",PLANNED:"PLANNED",UNAVAILABLE:"UNAVAILABLE",STALE:"STALE",UNKNOWN:"UNKNOWN"};
function StatusBadge({status}:{status:DataStatus}){return <span className={"status status-"+status.toLowerCase()}>{statuses[status]}</span>}

export default function App(){
 const [focus,setFocus]=useState(false); const [boardOpen,setBoardOpen]=useState(true); const [presence,setPresence]=useState<AvatarPresence>("COMPACT_3D");
 const active=useMemo(()=>demoWorkspace.objects.find(o=>o.id===demoWorkspace.workspace.activeObjectRef)!,[]);
 const knowledge=demoWorkspace.objects.find(o=>o.id==="demo:knowledge:mvp-principle")!;
 const cyclePresence=()=>setPresence(p=>p==="COMPACT_3D"?"EYES":p==="EYES"?"STATUS":p==="STATUS"?"HIDDEN":"COMPACT_3D");
 return <main className={focus?"app focus":"app"}>
   <header><div><b>FATHER</b><span> / ALINA CONTROL CENTER</span></div><StatusBadge status="DEMO"/></header>
   <aside className="rail left"><button>Knowledge</button><button>Sources</button><button>Projects</button><button>Agents</button></aside>
   <section className="stage">
     <div className={"alina "+presence.toLowerCase()} aria-label={"ALINA "+presence}>
       {presence!=="HIDDEN"&&<><div className="alina-face"><i/><i/></div><strong>ALINA</strong><small>ANALYST · {presence}</small></>}
     </div>
     <section className="table">
       <div className="table-label">WORK TABLE · {demoWorkspace.workspace.workTableMode}</div>
       <StatusBadge status={active.dataStatus}/><h1>{active.title}</h1><p>Первичный рабочий объект красивого MVP. Канонические данные пока не подключены.</p>
       <div className="meta">ID {active.id} · {active.version}</div>
     </section>
     {boardOpen&&<section className="board"><div><b>KNOWLEDGE</b> <StatusBadge status={knowledge.dataStatus}/></div><h2>{knowledge.title}</h2><p>Показываем человеку то, что нужно для текущего решения, а не всё, что знает система.</p><button onClick={()=>setBoardOpen(false)}>Свернуть табло</button></section>}
   </section>
   <aside className="rail right"><button onClick={()=>setFocus(v=>!v)}>{focus?"Выйти из Focus":"Focus Mode"}</button><button onClick={cyclePresence}>ALINA: {presence}</button>{!boardOpen&&<button onClick={()=>setBoardOpen(true)}>Открыть Knowledge</button>}</aside>
   <footer>DATA: DEMO · RENDER: TWO_D · Knowledge Core: NOT CONNECTED</footer>
 </main>
}
