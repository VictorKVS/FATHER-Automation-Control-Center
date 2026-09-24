import { useEffect, useMemo, useState } from "react";
import { demoWorkspace } from "./demoData";
import type { AvatarPresence, DataStatus } from "./types";
import { loadPresentationState, savePresentationState } from "./workspaceState";
import { AlinaScene } from "./AlinaScene";
import "./styles.css";

const statuses: Record<DataStatus,string>={REAL:"REAL",DEMO:"DEMO",PLANNED:"PLANNED",UNAVAILABLE:"UNAVAILABLE",STALE:"STALE",UNKNOWN:"UNKNOWN"};
function StatusBadge({status}:{status:DataStatus}){return <span className={"status status-"+status.toLowerCase()}>{statuses[status]}</span>}

export interface AppProps { avatarRendererAvailable?: boolean }

export default function App({avatarRendererAvailable=true}:AppProps){
 const restored=useMemo(()=>loadPresentationState(),[]);
 const [focus,setFocus]=useState(restored.focus);
 const [boardOpen,setBoardOpen]=useState(restored.boardOpen);
 const [presence,setPresence]=useState<AvatarPresence>(restored.presence);
 const active=useMemo(()=>demoWorkspace.objects.find(o=>o.id===demoWorkspace.workspace.activeObjectRef),[]);
 const knowledge=demoWorkspace.objects.find(o=>o.id==="demo:knowledge:mvp-principle");
 useEffect(()=>savePresentationState({focus,boardOpen,presence}),[focus,boardOpen,presence]);
 const cyclePresence=()=>setPresence(p=>p==="COMPACT_3D"?"EYES":p==="EYES"?"STATUS":p==="STATUS"?"HIDDEN":"COMPACT_3D");

 if(!active || !knowledge) return <main className="fatal-state"><StatusBadge status="UNAVAILABLE"/><h1>Workspace object unavailable</h1><p>DEMO fixture reference could not be resolved.</p></main>;

 return <main className={focus?"app focus":"app"}>
   <header><div><b>FATHER</b><span> / ALINA CONTROL CENTER</span></div><StatusBadge status="DEMO"/></header>
   <aside className="rail left"><button>Knowledge</button><button>Sources</button><button>Projects</button><button>Agents</button></aside>
   <section className="stage">
     {avatarRendererAvailable && <AlinaScene/>}
     {avatarRendererAvailable ? <div className={"alina "+presence.toLowerCase()} aria-label={"ALINA "+presence}>
       {presence!=="HIDDEN"&&<><div className="alina-face"><i/><i/></div><strong>ALINA</strong><small>ANALYST · {presence}</small></>}
     </div> : <div className="alina-fallback" role="status">ALINA · STATUS ONLY · RENDERER UNAVAILABLE</div>}
     <section className="table">
       <div className="table-label">WORK TABLE · {demoWorkspace.workspace.workTableMode}</div>
       <StatusBadge status={active.dataStatus}/><h1>{active.title}</h1><p>Первичный рабочий объект красивого MVP. Канонические данные пока не подключены.</p>
       <div className="meta">ID {active.id} · {active.version}</div>
     </section>
     {boardOpen&&<section className="board"><div><b>KNOWLEDGE</b> <StatusBadge status={knowledge.dataStatus}/></div><h2>{knowledge.title}</h2><p>Показываем человеку то, что нужно для текущего решения, а не всё, что знает система.</p><button onClick={()=>setBoardOpen(false)}>Свернуть табло</button></section>}
   </section>
   <aside className="rail right"><button onClick={()=>setFocus(v=>!v)}>{focus?"Выйти из Focus":"Focus Mode"}</button><button onClick={cyclePresence}>ALINA: {presence}</button>{!boardOpen&&<button onClick={()=>setBoardOpen(true)}>Открыть Knowledge</button>}</aside>
   <footer>DATA: DEMO · RENDER: {avatarRendererAvailable?"TWO_D":"STATUS_ONLY"} · Knowledge Core: NOT CONNECTED</footer>
 </main>
}
