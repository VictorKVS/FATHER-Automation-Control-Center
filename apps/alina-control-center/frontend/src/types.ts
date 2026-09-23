export type DataStatus = "REAL" | "DEMO" | "PLANNED" | "UNAVAILABLE" | "STALE" | "UNKNOWN";
export type AvatarPresence = "COMPACT_3D" | "EYES" | "STATUS" | "HIDDEN";
export interface FatherObject { id:string; type:string; title:string; version:string; dataStatus:DataStatus; provenanceRefs:string[]; relationRefs:string[] }
export interface BoardState { id:string; type:string; objectRef:string|null; state:"OPEN"|"PINNED"|"MINIMIZED"|"CLOSED"; relationToPrimary:string; dataStatus:DataStatus }
export interface WorkspaceState { version:string; activeObjectRef:string|null; workTableMode:string; openBoardIds:string[]; pinnedBoardIds:string[]; minimizedBoardIds:string[]; focusMode:boolean; avatarPresence:AvatarPresence; avatarPosition:string; renderMode:string }
export interface DemoWorkspace { fixtureVersion:string; dataStatus:"DEMO"; objects:FatherObject[]; boards:BoardState[]; workspace:WorkspaceState }
