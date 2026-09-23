import { describe,expect,it } from "vitest";
import { initialPresenceState, reducePresence } from "./presenceController";

describe("ALINA 3D Presence Controller P0",()=>{
  it("3D-001 starts at Work Table in idle full-body mode",()=>{
    expect(initialPresenceState).toMatchObject({mode:"FULL_BODY",behavior:"IDLE",anchor:"WORK_TABLE"});
  });

  it("3D-002 moves semantically without mutating task continuity",()=>{
    const next=reducePresence(initialPresenceState,{type:"MOVE_TO",anchor:"INFORMATION_WALL"});
    expect(next).toMatchObject({anchor:"INFORMATION_WALL",behavior:"WALKING",dialogueAvailable:true,taskContextAvailable:true});
  });

  it("3D-003 presents Evidence without fabricating evidence objects",()=>{
    const next=reducePresence(initialPresenceState,{type:"PRESENT",panel:"EVIDENCE"});
    expect(next).toMatchObject({presentedPanel:"EVIDENCE",behavior:"PRESENTING"});
    expect(Object.keys(next)).not.toContain("evidence");
  });

  it("3D-004 yields space to a full-screen workspace",()=>{
    const next=reducePresence(initialPresenceState,{type:"OPEN_FULLSCREEN",panel:"GRAPH"});
    expect(next).toMatchObject({fullscreenPanel:"GRAPH",mode:"COMPACT",dialogueAvailable:true,taskContextAvailable:true});
  });

  it("3D-005 hide/show does not create another task context",()=>{
    const hidden=reducePresence(initialPresenceState,{type:"HIDE_ALINA"});
    const shown=reducePresence(hidden,{type:"SHOW_ALINA",mode:"FULL_BODY"});
    expect(hidden.mode).toBe("HIDDEN");
    expect(shown).toMatchObject({mode:"FULL_BODY",taskContextAvailable:true,dialogueAvailable:true});
  });

  it("3D-006 renderer failure degrades to status only",()=>{
    const failed=reducePresence(initialPresenceState,{type:"RENDERER_FAILED"});
    expect(failed).toMatchObject({rendererAvailable:false,mode:"STATUS_ONLY",dialogueAvailable:true,taskContextAvailable:true});
    const attempted=reducePresence(failed,{type:"SHOW_ALINA",mode:"FULL_BODY"});
    expect(attempted.mode).toBe("STATUS_ONLY");
  });

  it("3D-010 closes full-screen without losing scene anchor",()=>{
    const atWall=reducePresence(initialPresenceState,{type:"MOVE_TO",anchor:"INFORMATION_WALL"});
    const full=reducePresence(atWall,{type:"OPEN_FULLSCREEN",panel:"EVIDENCE"});
    const restored=reducePresence(full,{type:"CLOSE_FULLSCREEN"});
    expect(restored.anchor).toBe("INFORMATION_WALL");
    expect(restored.fullscreenPanel).toBeNull();
  });
});
