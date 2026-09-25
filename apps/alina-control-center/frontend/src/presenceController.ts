export type PresenceMode = "FULL_BODY" | "COMPACT" | "VOICE_ONLY" | "HIDDEN" | "STATUS_ONLY";
export type BehaviorState = "IDLE" | "LISTENING" | "THINKING" | "WALKING" | "PRESENTING" | "SPEAKING" | "WARNING" | "WAITING";
export type SceneAnchor = "WORK_TABLE" | "INFORMATION_WALL" | "KNOWLEDGE_PANEL" | "GRAPH_PANEL" | "EVIDENCE_PANEL";
export type WorkspacePanel = "KNOWLEDGE" | "GRAPH" | "EVIDENCE";

export interface PresenceState {
  mode: PresenceMode;
  behavior: BehaviorState;
  anchor: SceneAnchor;
  lookAt: SceneAnchor | null;
  presentedPanel: WorkspacePanel | null;
  fullscreenPanel: WorkspacePanel | null;
  rendererAvailable: boolean;
  dialogueAvailable: boolean;
  taskContextAvailable: boolean;
}

export type PresenceCommand =
  | { type:"SHOW_ALINA"; mode:PresenceMode }
  | { type:"HIDE_ALINA" }
  | { type:"MOVE_TO"; anchor:SceneAnchor }
  | { type:"LOOK_AT"; target:SceneAnchor }
  | { type:"PRESENT"; panel:WorkspacePanel }
  | { type:"OPEN_FULLSCREEN"; panel:WorkspacePanel }
  | { type:"CLOSE_FULLSCREEN" }
  | { type:"SET_BEHAVIOR"; state:BehaviorState }
  | { type:"RENDERER_FAILED" }
  | { type:"RENDERER_RESTORED" };

export const initialPresenceState: PresenceState = {
  mode:"FULL_BODY",
  behavior:"IDLE",
  anchor:"WORK_TABLE",
  lookAt:null,
  presentedPanel:null,
  fullscreenPanel:null,
  rendererAvailable:true,
  dialogueAvailable:true,
  taskContextAvailable:true,
};

export function reducePresence(state:PresenceState, command:PresenceCommand):PresenceState {
  switch(command.type){
    case "SHOW_ALINA":
      return {...state,mode:state.rendererAvailable?command.mode:"STATUS_ONLY"};
    case "HIDE_ALINA":
      return {...state,mode:"HIDDEN"};
    case "MOVE_TO":
      return {...state,anchor:command.anchor,behavior:"WALKING"};
    case "LOOK_AT":
      return {...state,lookAt:command.target};
    case "PRESENT":
      return {...state,presentedPanel:command.panel,behavior:"PRESENTING"};
    case "OPEN_FULLSCREEN":
      return {...state,fullscreenPanel:command.panel,mode:state.mode==="FULL_BODY"?"COMPACT":state.mode};
    case "CLOSE_FULLSCREEN":
      return {...state,fullscreenPanel:null};
    case "SET_BEHAVIOR":
      return {...state,behavior:command.state};
    case "RENDERER_FAILED":
      return {...state,rendererAvailable:false,mode:"STATUS_ONLY"};
    case "RENDERER_RESTORED":
      return {...state,rendererAvailable:true};
  }
}
