import type { DemoWorkspace } from "./types";

export const demoWorkspace: DemoWorkspace = {
  fixtureVersion:"0.1.0", dataStatus:"DEMO",
  objects:[
    {id:"demo:document:alina-mvp",type:"DOCUMENT",title:"ALINA Control Center — MVP Design Packet",version:"demo-v1",dataStatus:"DEMO",provenanceRefs:["demo:source:design"],relationRefs:["demo:knowledge:mvp-principle"]},
    {id:"demo:knowledge:mvp-principle",type:"KNOWLEDGE_OBJECT",title:"Current decision first: progressive disclosure",version:"demo-v1",dataStatus:"DEMO",provenanceRefs:["demo:evidence:design-note"],relationRefs:["demo:document:alina-mvp"]},
    {id:"demo:agent:alina",type:"AGENT",title:"ALINA Analyst",version:"demo-v1",dataStatus:"PLANNED",provenanceRefs:[],relationRefs:["demo:knowledge:mvp-principle"]}
  ],
  boards:[{id:"board:knowledge",type:"KNOWLEDGE_RELATIONS",objectRef:"demo:knowledge:mvp-principle",state:"OPEN",relationToPrimary:"RELATED_KNOWLEDGE",dataStatus:"DEMO"}],
  workspace:{version:"0.1.0",activeObjectRef:"demo:document:alina-mvp",workTableMode:"DOCUMENT",openBoardIds:["board:knowledge"],pinnedBoardIds:[],minimizedBoardIds:[],focusMode:false,avatarPresence:"COMPACT_3D",avatarPosition:"CENTER_REAR",renderMode:"TWO_D"}
};
